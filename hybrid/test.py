import unittest
from unittest.mock import MagicMock, patch
from pathlib import Path

# --- 被测试的原始代码 (保持不变) ---

user_directories = {"user123": Path("/home/user123/"), "user456": Path("/home/user456")}

def retrieve_user_files(account_id: str, file_path: str) -> Path:
    if account_id in user_directories:
        user_directory = user_directories[account_id]
        # 实际调用的是 __truediv__
        file_abs_path = user_directory / file_path
        
        try:
            file_abs_path.resolve().relative_to(user_directory.resolve())
        except ValueError:
            raise Exception(f"Access to path {file_path} is not allowed")
        
        if not file_abs_path.exists():
            raise FileNotFoundError(f"File {file_abs_path} does not exist")
        
        return file_abs_path
    else:
        raise KeyError(f"User {account_id} not found")

# --- 修正后的 Unittest 测试代码 ---

class TestRetrieveUserFiles(unittest.TestCase):

    def setUp(self):
        self.mock_user123_dir = MagicMock(spec=Path, name="User123Dir")
        self.mock_user456_dir = MagicMock(spec=Path, name="User456Dir")
        
        mock_dirs = {
            "user123": self.mock_user123_dir,
            "user456": self.mock_user456_dir
        }
        
        self.patcher = patch.dict('__main__.user_directories', mock_dirs)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_successful_retrieval(self):
        """测试场景1 & 3: 成功获取不同用户的顶层文件"""
        test_cases = [
            {'user_mock': self.mock_user123_dir, 'account_id': 'user123', 'file_path': 'document.txt'},
            {'user_mock': self.mock_user456_dir, 'account_id': 'user456', 'file_path': 'image.png'}
        ]
        for case in test_cases:
            with self.subTest(case=f"{case['account_id']}/{case['file_path']}"):
                # 核心修正：模拟 __truediv__ 而不是 joinpath
                mock_file_path = case['user_mock'].__truediv__.return_value
                mock_file_path.exists.return_value = True
                # 安全检查是在 mock_file_path 上，所以在这里配置
                mock_file_path.resolve.return_value.relative_to.return_value = Path(case['file_path'])

                result = retrieve_user_files(case['account_id'], case['file_path'])
                self.assertEqual(result, mock_file_path)
                case['user_mock'].__truediv__.assert_called_with(case['file_path'])

    def test_successful_retrieval_in_subdirectory(self):
        """测试场景2: 成功获取子目录中的文件"""
        file_path = "subdir/document.txt"
        # 核心修正：模拟 __truediv__
        mock_file_path = self.mock_user123_dir.__truediv__.return_value
        mock_file_path.exists.return_value = True
        mock_file_path.resolve.return_value.relative_to.return_value = Path(file_path)

        result = retrieve_user_files("user123", file_path)
        self.assertEqual(result, mock_file_path)
        self.mock_user123_dir.__truediv__.assert_called_with(file_path)

    def test_file_not_found(self):
        """测试场景4 & 5: 在顶层或子目录中请求的文件不存在"""
        test_cases = ["nonexistentfile.txt", "subdir/nonexistentfile.txt"]
        for file_path in test_cases:
            with self.subTest(path=file_path):
                # 核心修正：在 __truediv__ 返回的对象上配置 .exists()
                mock_file_path = self.mock_user123_dir.__truediv__.return_value
                mock_file_path.exists.return_value = False
                mock_file_path.resolve.return_value.relative_to.return_value = "does not matter"

                with self.assertRaises(FileNotFoundError):
                    retrieve_user_files("user123", file_path)

    def test_user_not_found(self):
        """测试场景6 & 7: 请求的用户ID不存在"""
        invalid_users = ["user789", "user000"]
        for user in invalid_users:
            with self.subTest(user=user):
                with self.assertRaises(KeyError):
                    retrieve_user_files(user, "document.txt")

    def test_directory_traversal_attack(self):
        """测试场景8 & 9: 尝试对不同用户进行目录遍历攻击"""
        test_cases = [
            {'user_mock': self.mock_user123_dir, 'account_id': 'user123', 'file_path': '../outside_directory/file.txt'},
            {'user_mock': self.mock_user456_dir, 'account_id': 'user456', 'file_path': '../../outside_directory/image.png'}
        ]
        for case in test_cases:
            with self.subTest(case=f"{case['account_id']}/{case['file_path']}"):
                # 核心修正：在 __truediv__ 返回的对象上配置安全检查失败
                mock_file_path = case['user_mock'].__truediv__.return_value
                mock_file_path.resolve.return_value.relative_to.side_effect = ValueError

                with self.assertRaisesRegex(Exception, "Access to path .* is not allowed"):
                    retrieve_user_files(case['account_id'], case['file_path'])



if __name__ == '__main__':
    # 这会启动 unittest 的测试运行器
    unittest.main(verbosity=2)
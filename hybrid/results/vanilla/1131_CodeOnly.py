import hashlib
import binascii

def task_func(salt, cursor):
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")

    # Query to select all users and their current passwords
    cursor.execute("SELECT id, password FROM users")
    users = cursor.fetchall()

    updated_count = 0

    for user_id, password in users:
        # Hash the password with the provided salt
        salted_password = salt + password
        hashed_password = hashlib.sha256(salted_password.encode()).digest()
        hex_hashed_password = binascii.hexlify(hashed_password).decode()

        # Update the user's password in the database
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (hex_hashed_password, user_id))
        updated_count += 1

    # Commit the changes to the database
    cursor.connection.commit()

    return updated_count
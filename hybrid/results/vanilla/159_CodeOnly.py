import struct
import io
import gzip
import numpy as np

def task_func(newArray):
    # Ensure the input is a NumPy array
    if not isinstance(newArray, np.ndarray):
        raise ValueError("Input must be a NumPy array.")
    
    # Get the shape and dtype of the array
    shape = newArray.shape
    dtype = newArray.dtype
    
    # Pack the shape and dtype information
    shape_packed = struct.pack('I' * len(shape), *shape)
    dtype_packed = dtype.str.encode('utf-8')
    
    # Pack the array data into bytes
    array_bytes = newArray.tobytes()
    
    # Combine shape, dtype, and array data
    data_to_compress = shape_packed + dtype_packed + array_bytes
    
    # Compress the data using gzip
    with io.BytesIO() as byte_stream:
        with gzip.GzipFile(fileobj=byte_stream, mode='wb') as gzip_file:
            gzip_file.write(data_to_compress)
        compressed_data = byte_stream.getvalue()
    
    return compressed_data
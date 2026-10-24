def total_download_size(sizes):
    return sum(sizes)

assert total_download_size([120, 45, 35]) == 200
assert total_download_size([80]) == 80
assert total_download_size([]) == 0

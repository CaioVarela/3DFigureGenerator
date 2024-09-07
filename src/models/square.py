class Square:
    def square(l, pc):
        x = [pc[0] + l/2, pc[0] + l/2, pc[0], pc[0] - l/2, pc[0] - l/2, pc[0] - l/2, pc[0], pc[0] + l/2, pc[0] + l/2]
        y = [pc[1], pc[1] + l/2, pc[1] + l/2, pc[1] + l/2, pc[1], pc[1] - l/2, pc[1] - l/2, pc[1] - l/2, pc[1]]
        z = [pc[2], pc[2], pc[2], pc[2], pc[2], pc[2], pc[2], pc[2], pc[2]]
        
        return x, y, z
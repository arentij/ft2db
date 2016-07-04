t = int(input())
print('%.i' % int((t // 3600) % 24), '%.2i' % int((t % 3600) // 60), '%.2i' % int(t % 60), sep=":")

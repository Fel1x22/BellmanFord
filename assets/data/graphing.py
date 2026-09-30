import matplotlib.pyplot as plt

with open("output.txt", 'r') as file:
  full_data = [line.strip() for line in file]

xpoints = [i for i in range(10, 510, 10)]

data = []

for index in range(0, 250, 5):
  average = (float(full_data[index]) + float(full_data[index+1]) + float(full_data[index+2]) + float(full_data[index+3]) + float(full_data[index+4])) / 5
  data.append(average)

plt.figure(figsize=(10, 6))

plt.plot(xpoints, data, color='b')

plt.title('Bellman Ford Algorithm', fontsize=14)
plt.xlabel('Matrix Size (NxN)', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)

#plt.xscale("log")
#plt.yscale("log")

plt.xlim(0, 500)
plt.ylim(0, 10)



plt.grid(True)
plt.show()
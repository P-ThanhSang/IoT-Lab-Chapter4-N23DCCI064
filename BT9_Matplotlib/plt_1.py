import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = {
    "x": list(range(1, 10)),
    "y": [i**2 for i in range(1, 10)]
}

plt.plot(data['x'], data['y'], color='blue', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y = X^2')
plt.title('Line Chart - Y = X^2')
plt.grid(True, alpha=0.3)
plt.savefig('plt_1.png', dpi=150)
print('Saved: plt_1.png')

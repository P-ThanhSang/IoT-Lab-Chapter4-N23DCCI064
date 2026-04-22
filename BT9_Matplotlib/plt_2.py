import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = {
    "x": list(range(1, 10)),
    "y": [i**2 for i in range(1, 10)]
}

plt.scatter(data['x'], data['y'], marker='o', color='red', s=80)
plt.xlabel('X')
plt.ylabel('Y = X^2')
plt.title('Scatter Plot - Y = X^2')
plt.grid(True, alpha=0.3)
plt.savefig('plt_2.png', dpi=150)
print('Saved: plt_2.png')

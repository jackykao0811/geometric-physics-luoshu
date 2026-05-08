"""E8 angle comparison via SVD Lo-Shu principal axis."""
import numpy as np

# Lo-Shu principal axis via SVD
LUOSHU = np.array([[4,9,2],[3,5,7],[8,1,6]], dtype=float)
Lc = LUOSHU - 5
U, S, Vt = np.linalg.svd(Lc)
print(f"Singular values: {S}")
print(f"Principal vector: {Vt[0]}")
axis_angle = np.degrees(np.arctan2(Vt[0,1], Vt[0,0]))
print(f"Lo-Shu principal axis angle: {axis_angle:.4f} deg")

# E8 roots
roots = []
for i in range(8):
    for j in range(8):
        if i != j:
            for si in [1,-1]:
                for sj in [1,-1]:
                    r = np.zeros(8); r[i]=si; r[j]=sj
                    roots.append(r)
for mask in range(256):
    signs = np.array([1 if (mask>>k)&1==0 else -1 for k in range(8)])
    if np.sum(signs<0)%2 == 0:
        roots.append(signs/2)
roots = np.array(roots)
print(f"E8 roots: {len(roots)}")

# project to (x=col0, p=col1)
xy = roots[:, :2]
mag = np.linalg.norm(xy, axis=1)
nonz = mag > 1e-10
angles = np.degrees(np.arctan2(xy[nonz,1], xy[nonz,0])) % 360
# find most common cluster near 73-75 deg
target = 74.148
diffs = np.abs(angles - target)
diffs = np.minimum(diffs, 360-diffs)
closest = angles[np.argmin(diffs)]
print(f"Closest E8 angle to theta(1): {closest:.4f} deg")
print(f"theta(1) exact: 74.1484 deg")
print(f"Gap: {abs(closest-74.1484):.4f} deg")

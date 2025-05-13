# 📌 Point Tools – Blender Add-on

**Point Tools** is a Blender add-on for adding and exporting predefined named keypoints in your 3D scene. Ideal for character rigging, anatomical annotation, or structured scene marking.

---

## 🔧 Installation

1. Open **Blender**.
2. Go to **Edit > Preferences > Add-ons**.
3. Click **Install** in the top-right corner.
4. Select the `point_tools.py` file.
5. After installation, **check the box** to enable the add-on.
6. Close the Preferences window.

---

## 📍 Accessing the Tool

- Open the **3D Viewport**.
- Press `N` to open the **Sidebar**.
- Navigate to the **"Point Tools"** tab.

> Make sure you're in **Object Mode** to use the tool.

---

## 🛠 How to Use

### ➕ Add/Reset Keypoints

- Click **"Add/Reset Keypoints"** in the Point Tools panel.
- This will:
  - Delete any previously added keypoints.
  - Create a new root Empty object named `Keypoints`.
  - Add small spheres at each predefined location, parented to the root.

### 📤 Export to JSON

- Click **"Export Points (JSON)"**.
- Choose a save location and filename.
- A `.json` file will be saved containing the world-space coordinates of all keypoints.

---

## 📁 Exported JSON Format

```json
{
    "lfront_foot_tip": [x, y, z],
    "rfront_foot_tip": [x, y, z],
    "lfront_sesamoid": [x, y, z],
    "rfront_sesamoid": [x, y, z],
    ...
}

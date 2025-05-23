# 📌 Keypoint Tools – Blender Add-on

**Keypoint Tools** is a Blender add-on for adding and exporting predefined named keypoints in your 3D Horse Scans.

---

## 🔧 Installation
1. Clone the repo with `git clone https://github.com/TheDepe/blender_keypoint_annotation.git`
2. Compress the *entire* repo and get eg `blender_keypoint_annotation.zip`
1. Open **Blender**.
2. Go to **Edit > Preferences > Add-ons**.
3. Click **Install** in the top-right corner.
4. Select the `blender_keypoint_annotation.zip` file.
5. After installation, **check the box** to enable the add-on.
6. Close the Preferences window.

---

## 📍 Accessing the Tool

- Open the **3D Viewport**.
- Press `N` to open the **Sidebar**.
- Navigate to the **"Keypoint Tools"** tab.

---

## 🛠 How to Use

### ➕ Add/Reset Keypoints

- Click **"Add/Reset Keypoints"** in the Point Tools panel.
- This will:
  - Delete any previously added keypoints.
  - Create a new root Empty object named `Keypoints`.
  - Add small spheres at each predefined location, parented to the root.

<img src="assets/Keypoints.png" alt="List of Keypoints in Blender" width="400"/>

### 🧭 Position Keypoints (manual):
![KeypointsList](assets/AnnotatedScan.png)
- You can scale and rotate the `Keypoints` root object to align the keypoints with the imported mesh.
- You can individually select and adjust keypoints.

    #### Notes and Tips:
    - Keypoints are defined only by their location. Rotation/normals are not considered.
    - Feel free to delete keypoints if necessary
    - WARNING: In some cases `Blender` crashes upon exporting the `.json` file. Make sure you save your blender file beforehand.

#### Annotation Guide
![KeypointsList](assets/AnnotationGuide.png)

### 📤 Export to JSON

- Click **"Export Points (JSON)"**.
- **Choose** a save location and filename.
- A `.json` file will be saved containing the world-space coordinates of all keypoints.

---

## 📁 Exported JSON Format

```
{
    "lfront_foot_tip": [x, y, z],
    "rfront_foot_tip": [x, y, z],
    "lfront_sesamoid": [x, y, z],
    "rfront_sesamoid": [x, y, z],
    ...
}
```
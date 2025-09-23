
### `src/dataloading.py` (simple loader you can include)
```python
import os, json, numpy as np

def load_preprocessed(root="data/preprocessed"):
    feats = np.load(os.path.join(root, "image_features.npy"))
    with open(os.path.join(root, "image_map.json")) as f: image_map = json.load(f)
    with open(os.path.join(root, "captions_tokens.json")) as f: caps = json.load(f)
    with open(os.path.join(root, "word_to_idx.json")) as f: w2i = json.load(f)
    with open(os.path.join(root, "idx_to_word.json")) as f: i2w = json.load(f)
    with open(os.path.join(root, "train.json")) as f: train_ids = json.load(f)
    with open(os.path.join(root, "val.json")) as f: val_ids = json.load(f)
    with open(os.path.join(root, "test.json")) as f: test_ids = json.load(f)
    return feats, image_map, caps, w2i, i2w, train_ids, val_ids, test_ids

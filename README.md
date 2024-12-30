# Kingdom - AI Translation

# Character Processing Workflow

This repository outlines a step-by-step guide to process character tiles using Codeformer and embedding techniques. The goal is to identify missing characters and analyze them through their embeddings, with potential applications in linguistic research, font generation, and more.

## Workflow Steps

### 1. Process Tiles with Codeformer
Use [CodeFormer](https://huggingface.co/spaces/sczhou/CodeFormer) to enhance and refine character tiles. Apply the following settings for optimal results:

- **Preface Align**: 0  
- **Background Enhance**: 0  
- **Face_Upsample**: 0  
- **Rescaling_Factor**: 2  
- **Codeformer_Fidelity**: 1  

### 2. Separate Outputs into Individual Characters
Manually or programmatically extract individual characters from the processed tiles.

### 3. Embed Individual Characters
Embed each character using a suitable embedding model or technique. The embeddings will serve as unique representations of the characters, enabling advanced search and comparison functionalities.

### 4. Organize Characters by Embedding Closeness
Group characters into folders based on their embedding similarities using query search techniques. This step helps to organize and analyze characters efficiently.

---

## Mindmap and Use Case
A detailed **mindmap** for this process is available on Canva:  
[View Mindmap](https://www.canva.com/design/DAGV1eSB0b4/EiWCTgu--mjySh0PUQXaow/edit?referrer=mind-maps-landing-page)

### Application
This workflow simplifies the task of identifying missing characters by:
1. **Matching Word Variations**: Compares characters with removed vowels (as seen in modern Hebrew) using platforms like [Dabar Cloud](https://dabar.cloud).
2. **Mapping Similar Words**: Utilizes JSON-like mappings to identify words and suggest probable matches when interpretations are unclear.

---

## Future Possibilities
1. **Font-Like Structure with GANs**:
   - Use embeddings to create generative font-like structures.
   - Analyze the center of gravity of each letter for enhanced stability and retrievability.

2. **Word Probability Mapping**:
   - Infer potential word combinations by analyzing character mappings and their similarities.

---

### Contribution
Feel free to contribute to this repository by suggesting optimizations, adding new embedding techniques, or proposing additional use cases.

---
title:  "DynEval: Holistic Evaluations of T2I Generative Models in the Wild"
date:   2026-05-23 22:21:59 +00:00
image: /publications/images/dyneval-eccv-fig.png
authors: "Shyam Marjit*, <strong>Dheeraj Baiju*</strong>, Anuj Shikarkhane, Akhil Sakthieswaran, Sayak Paul, Anirban Chakraborty."
venue: "ECCV"
arxiv: "https://arxiv.org/abs/2607.11199"
project: "https://vcl-iisc.github.io/dyneval/"
code: "https://github.com/vcl-iisc/dyneval_code"
---
Recent advances in text-to-image (T2I) generation have led to models capable of producing highly realistic images. Yet, reliably evaluating their outputs remains challenging, especially at scale. Existing automatic evaluators, often relying on a static prompt set, struggle to capture subtle failure modes such as partial prompt misalignment, compositional errors or visually plausible but semantically incorrect generations. In this work, we introduce DynEval, a Dynamic Evaluation framework designed to jointly assess text-to-image alignment and image quality of T2I models. To support scalable training beyond limited human-annotated data, we construct two large datasets. First, we build GenDB,
a collection of 500K prompt-image pairs generated from human-written prompts drawn from DiffusionDB using a tiered prompt-model generation strategy. Second, building upon GenDB, we construct DynEvalInstruct, a 250K instruction dataset comprising prompt-image-response triplets distilled from a structured evaluation pipeline that decomposes
evaluation into text-image alignment and visual quality reasoning. Using
this dataset, we perform full fine-tuning of a compact evaluator through a curriculum learning strategy to effectively distill the superior evaluation capabilities of a larger teacher vision-language model, resulting in DynEval-2B and DynEval-4B. In extensive comparisons against existing evaluators across 11 benchmarks, our evaluator achieves a higher overall correlation with human judgments. Furthermore, it provides finegrained analysis of the capabilities and failure modes of 36 T2I models across 42 subcategories and 9 semantic dimensions.



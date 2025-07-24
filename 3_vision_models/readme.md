Vision Language Tasks

Image Captioning
Visual Question
Text to Image Generation

Components

 - model architecture
 - training strategy (loss function ,initialization, training stages (pretraining, fine-tuning))
 

 Model architectures

 I. Encoder / Decoder
 II. Dual Encoder
 III. Cross Modal
 IV. Natively MultiModal

I. Encoder/Decoder
 - from the same ones from NLP

 Welcome to Sarajevo -> input -> text encoder (embedding) -> decoder -> loss (bun venit in EEML in Sarajevo)

 A Neural Image Caption Generator

 Architecture 
 Encoder: CNN
 Decoder: RNN

 Training strategy: 
 Pretrain the CNN for image classification
 Drop the last CNN layer, and pass encoded image to RNN

 VQA

 Attach a text encoder near the visual encoder

II. Dual-Encoder

"Pigs" Text Input => Text Encoder -> Loss_1
Image (with Pigs) -> Visual Encoder -> Loss_1


CLIP: Contrastive Language - Image Pre-training

Contrastive loss

compute cosine similarities

images with dogs goat car 

probabilities

softmax

Image to text Contrastive objective

Applications of dual-encoder models

Images -> template: "A photo of {object}" -> Text Encoder 

Applications of dual encoder models

Using CLIP to detect cloth masks vs surgical masks

Timeline

Transformers 2017
ViT - 2021
CLiP - 2021

Advantages: Open vocabulary (zero-shot generalization)
Fast & Efficient: can compute image and text embeddings in parallel
Scalable: fast retrieval (over 5GB images)

Weaknesses - sensitive to prompt format
Image-level captions are insufficient supervision

III. Cross Modal

Comparison so far:
ENcoder decoder - no cross attention
- no shared embedding space

information bottleneck

Dual Encoder Models

no text generation
no cross attention

Cross Modal

Image -> Unimodal Visual Encoder ->(Cross Attention - attentional pooling) Multimodal Text Encoder -> LOss_1
Text -> Unimodal Text Encoder  -> Multimodal Text Encoder -> Loss_1




CoCa: Contrastive Captioners are Image-Text Foundation Models

Architecture:

Separate unimodal encoders with self attention
joint multimodal decoder with cross-attention

CoCa : Pretraining

L Coca = (take formula here)

Coca: Evaluation

CoCa(2022)

ChatGPT (2022)

LLAVA - Large Language and Vision Assistant

Motivation: LLM had become a game changer for language tasks, due to their world knowledge and ability to follow in instructions

Image => Vision Encoder -> Projection -> LLM (also q: Whare are pigs doing in the image ) -> Loss


Architecture

CLIP VIT-L / 14
Text Encoder: LLAMA
Projection: Linear

Training strategy:

1 Pretraining strage for feature alignment

Vision Encoder -> Pretrained
Text encoder -> Pretratined

Projector -> Trained for random init on captioning data

2) Fine-tuning End-to-End

LLAVA: INstruction Tuning Synthetic Data

images from COCO Dataset

Visual data translated into text. to prompt text-only GPT-4 model

GPT 4 Responses

LLAVA: Training


VLM Evaluation Today 

Vision Arena 

MMMU
VQA, GQA, OK-VQA

LLAVA: Summary

Among the first to use a vision encoder with an LLM
Generated synthetic training data

IV Natively MultiModal - 

Early fusion (input modalities converted into a common representational format: sequence of tokens or embeddings)\

Visual Encoder -> MultiModal_1 -> Loss_1
Audio Encoder -> MultiModal_1 -> Loss_1
Text -> MultiModal_1 -> Loss_1

Input Sequence -> Model (Gemini) -> Transformer -> Image Decoder
                                                -> Text Decoder


Training 

Large scale pretraining on multimodal, multilingual dataset
Supervised fine-tuning (SFT) on demonstration data
RLHF to align the model's outputs with human preferences

Natively Multimodal - 2023

Segmentation Models - Open Vocabulary Segmentation: Segment Anything
Text-toImage Generation - Diffusion Models
Transformer model followed by a cascade of diffusion models

Video-Language-Models

VLMs with Tools: Visual PRogramming
ViperGPT (paper that won competition)





                                            
# DIAA👩🏼‍⚕️(Diagnostic Intelligence Analytical Assistant)
<p align = "center"><img src="https://github.com/xnileshtiwari/DIAA-Diagnostic-Intelligence-Analytical-Assistant-/assets/135645478/68fe66f1-9050-4417-9647-448c77fa9572" alt="DIAA" width="400" height="auto">
</p>


_Imagine a world where every patient has instant access to a medical expert, 24/7. That’s what AMIE offers—an AI system optimized for diagnostic dialogue. It’s like having a virtual doctor in your pocket, one that learns from diverse medical conditions and dialogues to provide accurate diagnoses and empathetic communication. With AMIE, we’re not just creating technology; we’re crafting a future where quality healthcare is a conversation away. Whether you’re in a remote village or a bustling city, AMIE is your personal medical expert, always ready to assist._



Apologies for the inconvenience, but due to exhaustion of cloud credit, we won’t be able to provide a live demo. However, you can still view DIAA’s responses here.





## 📃Datasets used
- [MedQA](https://huggingface.co/datasets/bigbio/med_qa): This is the data and baseline source code for the paper: Jin, Di, et al. "What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams." `arXiv preprint arXiv:2009.13081 (2020).`
- [HealthSearchQA](https://github.com/abachaa/MedQuAD): MedQuAD `includes 47,457 medical question-answer pairs created from 12 NIH websites` (e.g. cancer.gov, niddk.nih.gov, GARD, MedlinePlus Health Topics). The collection covers 37 question types (e.g. Treatment, Diagnosis, Side Effects) associated with diseases, drugs and other medical entities such as tests.  

- [LiveQA](https://github.com/abachaa/LiveQA_MedicalTask_TREC2017): The LiveQA'17 medical task focuses on consumer health question answering. 
- [MedicationQA](https://www.kaggle.com/datasets/thedevastator/comprehensive-medical-q-a-dataset): The MedQuad dataset provides a comprehensive source of medical questions and answers for natural language processing. With `over 43,000 patient inquiries from real-life situations categorized into 31 distinct types of questions`, the dataset offers an invaluable opportunity to research correlations between treatments, chronic diseases, medical protocols and more.

- [MIMIC-III](https://physionet.org/content/mimiciii/1.4/): A dataset consisting of 65 clinician-written summaries of medical notes from MIMIC-III, a large, publicly available database containing medical records of intensive care unit patients, was used as additional training data for DIAA. `MIMIC-III contains approximately 2 million notes` spanning 13 types including cardiology, respiratory, radiology, physician, general, discharge, case management, consult, nursing, pharmacy, nutrition, rehabilitation and social work.

- <ins>**Custom Dataset using simulated AI Agents🤖**:</ins> In order to produce high-quality simulated dialogues at scale, we developed a novel multi-agent framework which comprised three key components:
  - `Vignette Generator:` AMIE leverages web searches to craft unique patient vignettes given a specific
medical condition.
  - `Simulated Dialogue Generator:` Three LLM agents play the roles of patient agent, doctor agent,
and moderator, engaging in a turn-by-turn dialogue simulating realistic diagnostic interactions.
  - `Self-play Critic:` A fourth LLM agent acts as a critic to give feedback to the doctor agent for self-improvement. Notably, AMIE acted as all agents in this framework.



## License

DIAA is released under the MIT License.

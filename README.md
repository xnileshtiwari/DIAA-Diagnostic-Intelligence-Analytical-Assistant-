# DIAA👩🏼‍⚕️(Diagnostic Intelligence Analytical Assistant)
<p align = "center"><img src="https://github.com/xnileshtiwari/DIAA-Diagnostic-Intelligence-Analytical-Assistant-/assets/135645478/68fe66f1-9050-4417-9647-448c77fa9572" alt="DIAA" width="400" height="auto">
</p>


_Imagine a world where every patient has instant access to a medical expert, 24/7. That’s what AMIE offers—an AI system optimized for diagnostic dialogue. It’s like having a virtual doctor in your pocket, one that learns from diverse medical conditions and dialogues to provide accurate diagnoses and empathetic communication. With AMIE, we’re not just creating technology; we’re crafting a future where quality healthcare is a conversation away. Whether you’re in a remote village or a bustling city, AMIE is your personal medical expert, always ready to assist._



**Apologies for the inconvenience, but due to exhaustion of cloud credit, we won’t be able to provide a live demo. However, <ins>you can still view DIAA’s responses here👇🏼.**</ins>

[![Testing DIAA’s reasoning ability](https://github.com/xnileshtiwari/DIAA-Diagnostic-Intelligence-Analytical-Assistant-/assets/135645478/c9f82974-2635-4d71-9b46-a779e2f25525)](https://youtu.be/-ueoiTlqqa8 "Testing DIAA")



## 📃Datasets used
- [MedQA](https://huggingface.co/datasets/bigbio/med_qa)
- [HealthSearchQA](https://github.com/abachaa/MedQuAD)
- [LiveQA](https://github.com/abachaa/LiveQA_MedicalTask_TREC2017)
- [MedicationQA](https://www.kaggle.com/datasets/thedevastator/comprehensive-medical-q-a-dataset)
- [MIMIC-III](https://physionet.org/content/mimiciii/1.4/)

- <ins>**Custom Dataset using simulated AI Agents🤖**:</ins> In order to produce high-quality simulated dialogues at scale, we developed a novel multi-agent framework which comprised three key components:
  - `Vignette Generator:` AMIE leverages web searches to craft unique patient vignettes given a specific
medical condition.
  - `Simulated Dialogue Generator:` Three LLM agents play the roles of patient agent, doctor agent,
and moderator, engaging in a turn-by-turn dialogue simulating realistic diagnostic interactions.
  - `Self-play Critic:` A fourth LLM agent acts as a critic to give feedback to the doctor agent for self-improvement. Notably, AMIE acted as all agents in this framework.

![processss](https://github.com/xnileshtiwari/DIAA-Diagnostic-Intelligence-Analytical-Assistant-/assets/135645478/2ca69a57-5877-4c0f-a8cb-29bd5c9bfca7)



## License
DIAA is released under the MIT License.

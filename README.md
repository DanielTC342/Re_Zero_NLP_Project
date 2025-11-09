# Narrative Memory AI — Re:Zero Project (Work in Progress)

## Project defintion

The current project was created to develop an episodic memory system for linguistic agents using structured narrative (in this case the first act of the novel "RE:ZERO STARTING A LIFE IN A DIFFERENT WORLD FROM ZERO" written by TAPPEI NAGATSUKI) to evaluate their capacity to retrieve past events, infer relations and simulate the consolidation of memories.

This linguistic agent will be capable to answer questions like "What did Subaru feel about Rem in the Arc n?", looking for relevant scenes in the arc and answer with it's own memory and not with external knoledge.

Also the linguistic agent should be capable to have memory (in a simulation).

### What is Narrative Memory

### What is RAG (Retrieval-Augmented Generation)?

### Project objectives

- Have an AI agent capable to retreive specific episodes when is necessary
- estudiar cómo el lenguaje (narrativa, re-encuadre, etiquetado emocional) transforma recuerdos episódicos en recuerdos más abstractos (semánticos), imitando la consolidación humana.
- combinar recuperación eficiente de recuerdos con gestión dinámica del contexto que se pasa al LLM (evitar saturación del prompt, priorizar lo relevante, controlar costes).

### Source of data and limitations

### Future perspectives

In the future the plan is to build an app similar to Character AI but especialized in Re Zero that accurarately emulates the behivor of the most important chracters of the novel (such as Subaru, Emilia, Rem, etc.) and with memory about the events they haven been through in the novel, so the AI character not only will answer as a "certain" character but act like that character and response about hypotethical situation in it's world.

## Project roadmap

The roadmap consist in three phase that globe the full live cycle of a research project.

### First Phase (ETL process and "memory building")

- Data extraction from the "Witch Cult Translations" using web scraping.
- Data transformations using data cleansing techniques and chunking.
- Data load in a vectorial data base using embeddings.

### Second Phase (RAG process)

- Build the "query engine".

### Third Phase (Test)

- Retrieval-based QA.
- Evaluation benchmarks.

## Author rights

The data use for this project BELONG TO TAPPEI NAGATSUKI, THE ORIGINAL AUTHOR OF RE:ZERO STARTING A LIFE IN A DIFFERENT WORLD FROM ZERO.

# Routing protocols in IoT wireless ad-hoc mesh networks

## Abstract

Wireless mesh networks (MANETs) are often used in IoT applications,
enabling quick and efficient deployment
while maintaining connectivity and robustness in changing conditions.
This scoping review protocol, guided by the PRISMA-ScR framework,
aims to explore the algorithms used for routing in such networks.
The review seeks to identify existing approaches, highlight challenges, evaluate effectiveness,
and uncover research gaps. By synthesizing the current body of knowledge,
this study will inform future developments in routing algorithm design,
focusing on scalable, autonomous, and efficient IoT systems.

## Introduction

Wireless mesh networks (MANETs) have become increasingly popular in IoT applications,
because they do not require any infrastructure apart from the devices themselves.
They are also increasingly being used to supplement or even replace traditional wireless infrastructure,
like Wi-Fi networks.
The performance characteristics of a MANET depend on a number of factors,
and a very important one is the routing methods being used in the network.

The main objective is to map existing approaches, identify key challenges,
and highlight unresolved research questions.
Through systematic identification and evaluation of relevant literature,
this review aims to provide a comprehensive understanding of how MANETs are conceptualized,
operationalized, and evaluated across different contexts.

### Rationale

The increasing complexity of IoT applications necessitates advanced approaches
to ensure efficient and fast routing and convergence in mesh networks.

As IoT devices are deployed in diverse applications and network conditions,
it is crucial to design and evaluate routing algorithms that are scalable,
robust and efficient in different scenarios.
Understanding existing methodologies and identifying research gaps is essential for advancing the field.

### Objectives

The primary objectives of this scoping review are:

RQ#1. Highlight common approaches to routing in wireless mesh networks.  
RQ#2. Identify strategies for data exchange between network peers.  
RQ#3. Determine the mechanisms that enable network convergence and remove network loops.
RQ#4. Assess the effectiveness of different frameworks and strategies.

### Scope of the Review

This review follows the PRISMA-ScR framework to explore algorithms used in routing in wireless mesh networks.
Through systematic identification and evaluation of relevant literature,
this review aims to provide a comprehensive understanding of how MANET routing is conceptualized,
operationalized, and evaluated across different contexts.

# Protocol
## Design

The review will be conducted in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews (PRISMA-ScR). There will be five stages in the review process: 
1. Identifying the research questions; 
2. Identifying relevant studies; 
3. Study selection;
4. Data extraction/charting the data;
5. Collating, summarizing, and reporting results.

### Stage 1: Identifying the Research Questions

A preliminary search of relevant literature was undertaken in one database (searching ScienceDirect) using the following queries:
`mesh network AND routing`, `wifi AND routing AND mesh`, `wireless AND mesh network`.

These findings were used to inform the background for the review, refine its scope, generate eligibility criteria, and develop the search strategy.

The following objectives and research questions were identified:
- Objective 1: Conceptualization
  - How are routing algorithms defined and conceptualized in the context of IoT networks?
  - What applications have been developed or studied?
  - What are the challenges in the design of IoT wireless mesh networks?
- Objective 2: Operationalization
  - What algorithms and protocols are commonly used?
  - What metrics are used to evaluate the effectiveness of these algorithms?
  - How are domain-specific challenges addressed in IoT (e.g., battery life, computational constraints)?
- Objective 3: Evaluation
  - How are the results of routing protocols evaluated in terms of accuracy and efficiency?
  - What methodologies are used to validate and compare the algorithms?
  - What is the success criterion for IoT wireless applications?

Through seeking to answer the above questions, we aim to identify gaps in the literature (Objective 4), which need to be addressed as part of future research on wireless mesh network routing.

### Stage 2: Identifying Relevant Studies
The "PCC" mnemonic (population, concept, and context) is recommended by the Joanna Briggs Institute to construct clear inclusion criteria for scoping review and identify the focus and context of the review (Table 1).

#### Population

All participants involved in the development and application of artificial intelligence methods for gene classification will be considered. This includes researchers, bioinformaticians, and data scientists working on genomics or related fields. Additionally, experts from adjacent disciplines, such as computational biology or medical genetics, who contribute to the development of machine learning and AI techniques for gene classification, may also be included.

#### Concept
In defining the concept for this review, several decisions were made to focus the scope (Table 1). Studies that investigate routing algorithms in the specific context of wireless mesh networks will be included.

To address Objective 1 (Conceptualization), we will consider primary studies, commentaries, and editorials that discuss theoretical frameworks, methods, and challenges in the design of IoT wireless mesh networks.

For Objectives 2 (Operationalization) and 3 (Evaluation), the review will focus on primary studies that involve the development of IoT devices and networks. These studies must involve a focus on routing or network maintenance. While the scope of these studies may vary between routing algorithms in specific or wireless networks in general, the core requirement is that they address the question of routing.

Studies will only be included if they:
 1. Provide sufficient detail about the routing algorithm in question and about its implementation and evaluation.
 2. Clearly define the objectives and methods, including the specific application that the algorithm is intended to address.

If studies do not have a focus on routing, or apply to a different type of network, they will be excluded. Additionally, if a study lacks sufficient methodological detail to assess its relevance to the research objectives, it will be reviewed with caution, and the ambiguity will be documented.

#### Context
Studies that address the design and evaluation of algorithms for routing in the context of IoT wireless mesh networks will be included. This encompasses research globally, addressing diverse challenges such as energy efficiency, convergence speed, resource usage and link utilization efficiency. The scope includes studies that analyze routing algorithms in the context of IoT wireless mesh networks.

Eligible studies include both qualitative and quantitative research, as well as commentaries and editorials discussing the challenges involved in network routing. Grey literature, such as technical reports or guidelines from research institutions, will also be included if they contribute to the conceptual or operational understanding of the routing algorithms being used in this domain.

Exclusion criteria include conference abstracts, non-peer-reviewed articles, and studies outside the area of IoT wireless mesh networks. Only articles published in English will be reviewed. The timespan is not limited because many older studies are still relevant and may provide insights into the evolution of routing algorithms.


[include: eligibility-criteria.md]


### Search Strategy
The search strategy will follow a structured approach to ensure comprehensive coverage of relevant literature. Databases such as ScienceDirect will be searched using keywords like "wireless", "mesh network", "MANET", along with their synonyms. Boolean operators and advanced search techniques will be employed to refine results. Reference lists of key articles will also be reviewed, and, if necessary, authors of primary studies will be contacted for additional data or clarification.

All retrieved articles will be managed using reference tools such as Zotero, with duplicates removed for streamlined screening and analysis. This method ensures the inclusion of high-quality studies addressing the application of wireless mesh network routing algorithms.

| Publication details | Associated question(s)                               |
| ------------------- | ---------------------------------------------------- |
| Study title         | -                                                    |
| Author(s)           | Who are the authors of the study/document?           |
| Year of publication | What year was the study/document published?          |
| Publication type    | Is the document an empirical study?                  |
| Origin              | What is the country of origin of the study/document? |

| General details  | Associated question(s)                                           |
| ---------------- | ---------------------------------------------------------------- |
| Aims/purpose     | What are the study/document aims?                                |
| Study design     | What is the study/document design?                               |
| Study setting    | What real-life or imaginary environment does the study describe? |
| Study population | What is the described IoT system?                                |

| Content                | Associated question(s)                                     |
| ---------------------- | ---------------------------------------------------------- |
| Methodology details    | What IoT devices are being used?                           |
|                        | What are the main considerations for network routing?      |
|                        | Algorithm description                                      |
|                        | Is the algorithm domain-specific?                          |
| Measuring the outcomes | How is "success" defined?                                  |
|                        | How is the MANET evaluated?                                |
|                        | What are the benefits of the provided algorithm?           |

### Stage 3: Study Selection
The review process will be carried out by the reviewer in two stages. Titles and abstracts will be considered first; at this stage, some articles will be screened out. Depending on the results of the first stage of the review, AI methods may be employed to help screen the articles.
Articles that meet the inclusion/exclusion criteria will be included in the full-text review. If, based on the results of the first stage of the review, it is unclear whether to include the article, it will be included in the full-text review. The final search results will be presented in the PRISMA flowchart from PRISMA-ScR.

### Stage 4: Charting the Data
Data will be extracted into a spreadsheet program following guidelines from the Joanna Briggs Institute (JBI). Each member will extract data for a proportion of articles.

The data that will be extracted, will include the characteristics of the studies relevant to our research questions. The information to be extracted (Table 2) is consistent with the objectives of the analysis and is intended to reflect key findings relevant to the issue(s) under consideration.
 
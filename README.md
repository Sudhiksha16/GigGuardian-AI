# GigGuardian AI

## Overview
GigGuardian AI is an AI-powered parametric insurance platform designed to protect gig workers from income loss caused by external disruptions such as extreme weather, pollution, and city restrictions.

Delivery partners rely heavily on daily earnings, and unexpected disruptions can significantly affect their ability to work. GigGuardian AI provides a smart system that detects such disruptions and automatically compensates workers for their income loss.

---

## Problem Statement
Gig workers, especially food delivery partners from platforms like Swiggy and Zomato, depend on continuous work availability to earn their daily income.

However, external factors such as:

- Heavy rainfall  
- Floods  
- Extreme heat  
- Pollution alerts  
- Strikes or city restrictions  

can reduce or completely stop deliveries, causing significant income loss. Currently, gig workers have limited protection against these unpredictable events.

---

## Proposed Solution
GigGuardian AI provides an intelligent income protection platform for gig workers.

The system uses AI models and external data sources to detect disruptions in real time. When a disruption event exceeds predefined thresholds, the platform automatically triggers an insurance claim and processes instant payouts.

This parametric insurance model ensures that workers receive financial protection without lengthy claim processes.

---

## Weekly Premium Model
GigGuardian AI follows a **weekly micro-insurance pricing model** designed specifically for gig workers.

The premium is dynamically calculated based on:

- Historical weather risks
- Pollution levels in the worker’s operating area
- Frequency of disruptions in that location
- Delivery demand patterns

Workers can activate coverage for a specific week by paying a small premium, ensuring income protection during high-risk periods.

---

## Key Features
- Verified gig worker registration  
- AI-based disruption risk analysis  
- Delivery demand heatmap visualization  
- Gig Safety Index for risk awareness  
- Parametric insurance claim automation  
- Fraud detection using AI  
- Instant payout simulation  

---

## System Workflow
1. Worker registers on the platform  
2. Worker identity is verified  
3. AI analyzes disruption risk for the worker’s location  
4. Weekly insurance premium is calculated  
5. System monitors real-time disruption data  
6. Parametric triggers detect disruption events  
7. Automatic claim processing is initiated  
8. Worker receives instant payout  

---

## Technology Stack
**Frontend:** React / Flutter  
**Backend:** Node.js / Express  
**Database:** MongoDB  
**AI Models:** Python (Scikit-learn)  
**APIs:** Weather API, Maps API  

---

## AI Risk Prediction
GigGuardian AI uses machine learning models to analyze historical disruption data such as weather patterns, pollution levels, and delivery demand.

These models help estimate disruption probability in specific locations and enable dynamic risk assessment and premium adjustment.

---

## Project Structure

```
GigGuardian-AI
│
├ README.md
│
├ docs
│   ├ architecture-diagram.png
│   └ workflow-diagram.png
│
├ ui-design
│   ├ dashboard.png
│   ├ demand-heatmap.png
│   └ claim-notification.png
│
└ demo-video
    └ video-link.txt
```
---

## System Workflow Diagram

![Workflow](docs/workflow-diagram.png)

---

## System Architecture

![Architecture](docs/architecture-diagram.png)

---

## Expected Impact

GigGuardian AI aims to provide financial stability for gig workers by protecting them from income loss caused by unpredictable external disruptions.

By automating risk detection, claim triggering, and payouts, the platform reduces financial uncertainty for gig workers and strengthens the resilience of the gig economy.

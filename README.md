# Serving-LLM-model-with-Ray-Serve

This repository demonstrates how to serve a Large Language Model (LLM) using Ray Serve. The project leverages the facebook/blenderbot-400M-distill model for chat functionality and integrates translation services between English and Azerbaijani using the ray and ray[serve] frameworks.

## Project Overview
The project sets up a multilingual chat service with the following capabilities:

*  Chat: Utilizes the facebook/blenderbot-400M-distill model for generating responses to user inputs.
*  Translation: Includes services to translate messages between English and Azerbaijani.

## Key Components
Chat Service: Provides conversational AI capabilities using a pre-trained language model.
Translation Services: Translates messages from English to Azerbaijani and vice versa.

## Ray Serve
Ray Serve is a scalable and flexible model serving library built on Ray. It offers several advantages:

* Scalability: Easily scale model inference across multiple nodes.
* Flexibility: Serve multiple models and complex pipelines with minimal code changes.
* Ease of Use: Simplifies deployment of machine learning models in production environments.

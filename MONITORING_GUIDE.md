# Monitoring Guide

## 1. Purpose

This guide explains how the Road Maintenance Risk Prediction API is monitored after deployment.

The goal is to track:

- API activity
- prediction requests
- response time
- errors
- model behavior
- possible data drift
- when retraining may be needed

---

## 2. Log Location

The API stores logs in:

```text
logs/api.log
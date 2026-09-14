# Function That Returns Sorted Values

## Context

A development team working on a data science system for logistics is creating basic tools to analyze sensor performance samples. As part of the feature, they need a simple algorithm that sorts manually recorded values. To make the code reusable, the team decided to encapsulate the sorting logic inside a function that will run directly in a notebook, without external libraries. The returned result will be used to validate trends and detect future anomalies.

## Objective

Build a function that receives a list of numbers, sorts its values from smallest to largest using `for` loops and conditional swaps, and returns the new sorted list.

## Task

- Create a function called `sort_values(values)` that:
  - Receives a list of integer or decimal numbers.
  - Sorts the values from smallest to largest using `for` loops and conditional swap logic (`if`, `for`, and `range`).
  - Returns the sorted list.
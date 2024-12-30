# Catalog Placements Assignment

This repository contains a Java implementation of a simplified Shamir's Secret Sharing algorithm for decoding polynomials from JSON-encoded roots.

## Files

- **Main.java** - Provides output for both `input1.json` and `input2.json` simultaneously.
- **Main1.java** - Outputs results specifically for `input1.json`.
- **Main2.java** - Outputs results specifically for `input2.json`.

## Usage

To compile the files, use:

```shell
javac -cp ".;lib/json.jar" Main.java Main1.java Main2.java
java -cp ".;lib/json.jar" Main     # Runs both test cases together
java -cp ".;lib/json.jar" Main1    # Runs input1.json only
java -cp ".;lib/json.jar" Main2    # Runs input2.json only

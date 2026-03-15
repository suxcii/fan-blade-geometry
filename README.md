# fan-blade-geometry
Interactive visualization exploring the geometry and design of fan blades using SVG and JavaScript.

# Fan Blade Geometry Visualizer

## Overview

This project is an interactive website that explores how **geometry influences the design and efficiency of fan blades**. The site demonstrates how mathematical curves, symmetry, and rotation can be used to design fan blades that are both functional and visually appealing.

The design of the website is inspired by a **concentric spiral layout**, where blades emerge from a central hub and curve outward. This approach reflects the relationship between **mathematical beauty and practical engineering**, showing how geometry can guide airflow efficiency and structural balance.

Users can experiment with different blade parameters and observe how geometric changes influence the overall fan structure.

---

## Features

* Interactive blade designer
* Adjustable blade count
* Radius and twist controls
* SVG visualizations of fan geometry
* Demonstrations of multiple blade styles:

  * Straight blades
  * Twisted blades
  * Curved blades
  * Spiral inspired blades

---

## Purpose

The goal of this project is to explore how **geometric patterns appear in real world engineering design**. Fan blades rely on mathematical ideas such as:

* rotational symmetry
* curvature
* spiral patterns
* geometric transformations

These principles help engineers maximize airflow while minimizing energy consumption. This project demonstrates how these ideas can be visualized through interactive graphics.

---

## Project Structure

```
fanbladewebsite
│
├── app.py
├── index.html
│
├── static
│   ├── css
│   │   └── styles.css
│   │
│   └── js
│       ├── main.js
│       ├── blade-paths.js
│       ├── drawnFan.js
│       ├── interactive.js
│       └── svg.utils.js
│
└── .venv
```

---

## Files

### app.py

Runs a lightweight **Flask server** used for running the website locally during development.

### index.html

The main webpage that contains the structure of the site and loads the CSS styling and JavaScript files.

### static/css/styles.css

Controls the visual design of the website including layout, color scheme, typography, and page styling.

### static/js/main.js

Handles the main program logic responsible for generating and updating the fan blade visualization.

### static/js/blade-paths.js

Contains functions that compute the **geometric paths** used to create the blade shapes.

### static/js/drawnFan.js

Responsible for rendering the fan blades using **SVG graphics** so the shapes scale smoothly.

### static/js/interactive.js

Implements the interactive controls that allow users to adjust blade parameters and dynamically update the fan design.

### static/js/svg.utils.js

Contains helper functions used when working with SVG elements and geometric transformations.

### .venv

The Python virtual environment used to manage dependencies for the Flask development server.

---

## Technologies Used

* HTML
* CSS
* JavaScript
* SVG Graphics
* Python (Flask for local development)
* GitHub Pages for deployment

---

## Live Website

View the project here:

https://suxcii.github.io/fan-blade-geometry/

---

## Author

**Success Idemudia**

Created as part of a **Geometry in the World** midterm project exploring how mathematics shapes real world design and engineering.

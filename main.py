import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Generative Poster",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 Web-based Generative Poster")
st.write("Create your own generative poster.")

# Sidebar controls
st.sidebar.header("Poster Settings")

layers = st.sidebar.slider(
    "Layers",
    min_value=5,
    max_value=40,
    value=20
)

radius = st.sidebar.slider(
    "Radius",
    min_value=1.0,
    max_value=10.0,
    value=5.0
)

wobble = st.sidebar.slider(
    "Wobble",
    min_value=0.0,
    max_value=2.0,
    value=0.5
)

seed = st.sidebar.number_input(
    "Seed",
    min_value=0,
    max_value=9999,
    value=42
)

style = st.sidebar.selectbox(
    "Color Style",
    ["Pastel", "Vivid", "Mono"]
)

if st.button("Generate Poster"):

    np.random.seed(seed)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Color palettes
    if style == "Pastel":
        colors = [
            "#FFB6C1",
            "#FFDAB9",
            "#BDE0FE",
            "#CDEAC0",
            "#D8B4FE"
        ]

    elif style == "Vivid":
        colors = [
            "#FF006E",
            "#FB5607",
            "#FFBE0B",
            "#3A86FF",
            "#8338EC"
        ]

    else:
        colors = [
            "#222222",
            "#555555",
            "#888888",
            "#BBBBBB",
            "#DDDDDD"
        ]

    # Generate poster
    for i in range(layers):

        theta = np.linspace(
            0,
            2 * np.pi,
            200
        )

        current_radius = (
            radius
            * (1 - i / (layers * 1.5))
        )

        noise = np.random.normal(
            0,
            wobble,
            len(theta)
        )

        r = current_radius + noise

        x = r * np.cos(theta)
        y = r * np.sin(theta)

        ax.plot(
            x,
            y,
            color=colors[i % len(colors)],
            linewidth=2
        )

    ax.set_aspect("equal")
    ax.axis("off")

    st.pyplot(fig)

    st.success("Poster generated successfully!")

import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    # 23f3004197@ds.study.iitm.ac.in
    import marimo as mo
    import pandas as pd
    import plotly.express as px

    return mo, px


@app.cell
def _(mo, px):
    # Load the gapminder dataset from plotly's built-in datasets.
    # The 'data' DataFrame is created here and will be used by the
    # filtering cell below.
    data = px.data.gapminder()
    # Create an interactive slider for selecting the year.
    # The 'year_slider' object created here is a UI element that will be
    # available to other cells. Its '.value' attribute holds the currently
    # selected year.
    year_slider = mo.ui.slider(
        start=1952, stop=2007, step=5, value=1952, label="Select Year:"
    )

    # Display the slider in the notebook output.
    year_slider
    return data, year_slider


@app.cell
def _(mo, year_slider):
    # Data Flow: This cell depends on 'year_slider' from Cell 1.
    # It creates a dynamic title that updates whenever the slider is moved.
    mo.md(f"""
        ## Global Life Expectancy vs. GDP per Capita ({year_slider.value})
        This chart shows the relationship between Gross Domestic Product (GDP)
        per capita and life expectancy for the year **{year_slider.value}**.
        Each bubble represents a country.
    """)
    return


@app.cell
def _(data, year_slider):
    # Data Flow: This cell depends on 'data' from Cell 2 and
    # 'year_slider.value' from Cell 1.
    # It filters the main DataFrame based on the slider's current value.
    # The resulting 'filtered_data' is used by the plotting cell below.

    filtered_data = data[data["year"] == year_slider.value]

    return (filtered_data,)


@app.cell
def _(filtered_data, px):
    # Data Flow: This cell depends on 'filtered_data' from Cell 4.
    # It uses the filtered data to generate a scatter plot. When 'filtered_data'
    # changes, this cell automatically updates the plot.
    fig = px.scatter(
        filtered_data,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=60,
        labels={
            "gdpPercap": "GDP per Capita (log scale)",
            "lifeExp": "Life Expectancy (years)",
            "continent": "Continent",
        },
    )

    # Display the plotly figure.
    fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

import plotly.express as px


def main():
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    fig.show()


if __name__ == "__main__":
    main()

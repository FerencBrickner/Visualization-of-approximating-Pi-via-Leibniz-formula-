import matplotlib.pyplot as plt
from typing import Callable

type number = int | float
type FunctionToComputeGeneralTerm = Callable[[number], number]


def setup_plot(
    *,
    x_label: str = "Stepcount",
    y_label: str = "Approximation of Pi",
    figure_title: str = "Approximation of Pi via Leibniz formula",
) -> None:
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(figure_title)


def create_subsequent_leibniz_pi_approximations(
    stepcount: int = 200,
    compute_general_term: FunctionToComputeGeneralTerm = lambda x: 4
    * (-1) ** x
    / (2 * x + 1),
    current_approximation_of_pi: number = 0,
    approximations: list[number] = list(),
) -> list[number]:
    for step in range(stepcount):
        current_approximation_of_pi += compute_general_term(step)
        approximations.append(current_approximation_of_pi)
    return approximations


def plot_approximations(
    *,
    approximations: list[number],
    point_color: str = "blue",
    line_color: str = "orange",
    point_size: number = 3,
) -> None:
    x_coordinates: list[number] = list(range(len(approximations)))
    y_coordinates: list[number] = approximations
    plt.scatter(x_coordinates, y_coordinates, c=point_color, s=point_size)
    plt.step(x_coordinates, y_coordinates, c=line_color)


def main(*args, **kwargs) -> None:
    """
    Compute and plot approximations of Pi via the Leibniz formula.
    """
    setup_plot()
    subsequent_leibniz_pi_approximations = create_subsequent_leibniz_pi_approximations()
    plot_approximations(approximations=subsequent_leibniz_pi_approximations)
    plt.show()


if __name__ == "__main__":
    main()

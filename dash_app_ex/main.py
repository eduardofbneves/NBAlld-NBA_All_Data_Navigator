from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
import os.path

from src.components.layout import create_layout
from src.data.loader import load_dataframe, path_to_data


def main() -> None:
    team_season_stats = load_dataframe(path_to_data('team_season_stats'))
    team = load_dataframe(path_to_data('team'))
    app = Dash(__name__)
    app.title = "Test"
    app.layout = create_layout(app, [team, team_season_stats])
    app.run()


if __name__ == "__main__":
    main()

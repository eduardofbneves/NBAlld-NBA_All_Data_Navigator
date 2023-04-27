import os
from utils.loader import load_dataframe

def main() -> None:
    common_player_info = load_dataframe('common_player_info')
    print(common_player_info.loc[common_player_info['person_id']
                                      == 51])
    


if __name__ == "__main__":
    main()
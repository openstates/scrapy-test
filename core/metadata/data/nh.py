from ..models import State, Chamber, District, simple_numbered_districts

NH = State(
    name="New Hampshire",
    abbr="NH",
    capital="Concord",
    capital_tz="America/New_York",
    fips="33",
    unicameral=False,
    legislature_name="New Hampshire General Court",
    legislature_organization_id="ocd-organization/d8dce079-d59d-407c-be93-9d3fce72bd48",
    executive_name="Office of the Governor",
    executive_organization_id="ocd-organization/59217435-34d3-59ec-9673-733ae8b276d3",
    division_id="ocd-division/country:us/state:nh",
    jurisdiction_id="ocd-jurisdiction/country:us/state:nh/government",
    url="http://gencourt.state.nh.us",
    lower=Chamber(
        chamber_type="lower",
        name="House",
        organization_id="ocd-organization/3b857974-4029-4508-94d4-ce3b86c64602",
        num_seats=400,
        title="Representative",
        districts=[
            District(
                "Belknap 1",
                "lower",
                "ocd-division/country:us/state:nh/sldl:belknap_1",
                1,
            ),
            District(
                "Belknap 2",
                "lower",
                "ocd-division/country:us/state:nh/sldl:belknap_2",
                2,
            ),
            District(
                "Belknap 3",
                "lower",
                "ocd-division/country:us/state:nh/sldl:belknap_3",
                1,
            ),
            District(
                "Belknap 4",
                "lower",
                "ocd-division/country:us/state:nh/sldl:belknap_4",
                1,
            ),
            District(
                "Belknap 5",
                "lower",
                "ocd-division/country:us/state:nh/sldl:belknap_5",
                4,
            ),
            District(
                "Belknap 6",
                "lower",
                "ocd-division/country:us/state:nh/sldl:belknap_6",
                4,
            ),
            District(
                "Belknap 7",
                "lower",
                "ocd-division/country:us/state:nh/sldl:belknap_7",
                3,
            ),
            District(
                "Belknap 8",
                "lower",
                "ocd-division/country:us/state:nh/sldl:belknap_8",
                2,
            ),
            District(
                "Carroll 1",
                "lower",
                "ocd-division/country:us/state:nh/sldl:carroll_1",
                3,
            ),
            District(
                "Carroll 2",
                "lower",
                "ocd-division/country:us/state:nh/sldl:carroll_2",
                2,
            ),
            District(
                "Carroll 3",
                "lower",
                "ocd-division/country:us/state:nh/sldl:carroll_3",
                2,
            ),
            District(
                "Carroll 4",
                "lower",
                "ocd-division/country:us/state:nh/sldl:carroll_4",
                2,
            ),
            District(
                "Carroll 5",
                "lower",
                "ocd-division/country:us/state:nh/sldl:carroll_5",
                1,
            ),
            District(
                "Carroll 6",
                "lower",
                "ocd-division/country:us/state:nh/sldl:carroll_6",
                2,
            ),
            District(
                "Carroll 7",
                "lower",
                "ocd-division/country:us/state:nh/sldl:carroll_7",
                1,
            ),
            District(
                "Carroll 8",
                "lower",
                "ocd-division/country:us/state:nh/sldl:carroll_8",
                2,
            ),
            District(
                "Cheshire 1",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_1",
                1,
            ),
            District(
                "Cheshire 2",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_2",
                1,
            ),
            District(
                "Cheshire 3",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_3",
                1,
            ),
            District(
                "Cheshire 4",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_4",
                1,
            ),
            District(
                "Cheshire 5",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_5",
                1,
            ),
            District(
                "Cheshire 6",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_6",
                2,
            ),
            District(
                "Cheshire 7",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_7",
                1,
            ),
            District(
                "Cheshire 8",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_8",
                1,
            ),
            District(
                "Cheshire 9",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_9",
                1,
            ),
            District(
                "Cheshire 10",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_10",
                2,
            ),
            District(
                "Cheshire 11",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_11",
                1,
            ),
            District(
                "Cheshire 12",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_12",
                1,
            ),
            District(
                "Cheshire 13",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_13",
                1,
            ),
            District(
                "Cheshire 14",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_14",
                1,
            ),
            District(
                "Cheshire 15",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_15",
                2,
            ),
            District(
                "Cheshire 16",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_16",
                1,
            ),
            District(
                "Cheshire 17",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_17",
                1,
            ),
            District(
                "Cheshire 18",
                "lower",
                "ocd-division/country:us/state:nh/sldl:cheshire_18",
                2,
            ),
            District(
                "Coos 1", "lower", "ocd-division/country:us/state:nh/sldl:coos_1", 2
            ),
            District(
                "Coos 2", "lower", "ocd-division/country:us/state:nh/sldl:coos_2", 1
            ),
            District(
                "Coos 3", "lower", "ocd-division/country:us/state:nh/sldl:coos_3", 1
            ),
            District(
                "Coos 4", "lower", "ocd-division/country:us/state:nh/sldl:coos_4", 1
            ),
            District(
                "Coos 5", "lower", "ocd-division/country:us/state:nh/sldl:coos_5", 2
            ),
            District(
                "Coos 6", "lower", "ocd-division/country:us/state:nh/sldl:coos_6", 1
            ),
            District(
                "Coos 7", "lower", "ocd-division/country:us/state:nh/sldl:coos_7", 1
            ),
            District(
                "Grafton 1",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_1",
                3,
            ),
            District(
                "Grafton 2",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_2",
                1,
            ),
            District(
                "Grafton 3",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_3",
                1,
            ),
            District(
                "Grafton 4",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_4",
                1,
            ),
            District(
                "Grafton 5",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_5",
                2,
            ),
            District(
                "Grafton 6",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_6",
                1,
            ),
            District(
                "Grafton 7",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_7",
                1,
            ),
            District(
                "Grafton 8",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_8",
                3,
            ),
            District(
                "Grafton 9",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_9",
                1,
            ),
            District(
                "Grafton 10",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_10",
                1,
            ),
            District(
                "Grafton 11",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_11",
                1,
            ),
            District(
                "Grafton 12",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_12",
                4,
            ),
            District(
                "Grafton 13",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_13",
                1,
            ),
            District(
                "Grafton 14",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_14",
                1,
            ),
            District(
                "Grafton 15",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_15",
                1,
            ),
            District(
                "Grafton 16",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_16",
                1,
            ),
            District(
                "Grafton 17",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_17",
                1,
            ),
            District(
                "Grafton 18",
                "lower",
                "ocd-division/country:us/state:nh/sldl:grafton_18",
                1,
            ),
            District(
                "Hillsborough 1",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_1",
                4,
            ),
            District(
                "Hillsborough 2",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_2",
                7,
            ),
            District(
                "Hillsborough 3",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_3",
                3,
            ),
            District(
                "Hillsborough 4",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_4",
                3,
            ),
            District(
                "Hillsborough 5",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_5",
                3,
            ),
            District(
                "Hillsborough 6",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_6",
                3,
            ),
            District(
                "Hillsborough 7",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_7",
                3,
            ),
            District(
                "Hillsborough 8",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_8",
                3,
            ),
            District(
                "Hillsborough 9",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_9",
                3,
            ),
            District(
                "Hillsborough 10",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_10",
                3,
            ),
            District(
                "Hillsborough 11",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_11",
                3,
            ),
            District(
                "Hillsborough 12",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_12",
                8,
            ),
            District(
                "Hillsborough 13",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_13",
                6,
            ),
            District(
                "Hillsborough 14",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_14",
                2,
            ),
            District(
                "Hillsborough 15",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_15",
                2,
            ),
            District(
                "Hillsborough 16",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_16",
                2,
            ),
            District(
                "Hillsborough 17",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_17",
                2,
            ),
            District(
                "Hillsborough 18",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_18",
                2,
            ),
            District(
                "Hillsborough 19",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_19",
                2,
            ),
            District(
                "Hillsborough 20",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_20",
                2,
            ),
            District(
                "Hillsborough 21",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_21",
                2,
            ),
            District(
                "Hillsborough 22",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_22",
                2,
            ),
            District(
                "Hillsborough 23",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_23",
                2,
            ),
            District(
                "Hillsborough 24",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_24",
                2,
            ),
            District(
                "Hillsborough 25",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_25",
                2,
            ),
            District(
                "Hillsborough 26",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_26",
                2,
            ),
            District(
                "Hillsborough 27",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_27",
                1,
            ),
            District(
                "Hillsborough 28",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_28",
                2,
            ),
            District(
                "Hillsborough 29",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_29",
                4,
            ),
            District(
                "Hillsborough 30",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_30",
                3,
            ),
            District(
                "Hillsborough 31",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_31",
                1,
            ),
            District(
                "Hillsborough 32",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_32",
                3,
            ),
            District(
                "Hillsborough 33",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_33",
                2,
            ),
            District(
                "Hillsborough 34",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_34",
                3,
            ),
            District(
                "Hillsborough 35",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_35",
                2,
            ),
            District(
                "Hillsborough 36",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_36",
                2,
            ),
            District(
                "Hillsborough 37",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_37",
                1,
            ),
            District(
                "Hillsborough 38",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_38",
                2,
            ),
            District(
                "Hillsborough 39",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_39",
                2,
            ),
            District(
                "Hillsborough 40",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_40",
                4,
            ),
            District(
                "Hillsborough 41",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_41",
                3,
            ),
            District(
                "Hillsborough 42",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_42",
                3,
            ),
            District(
                "Hillsborough 43",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_43",
                4,
            ),
            District(
                "Hillsborough 44",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_44",
                2,
            ),
            District(
                "Hillsborough 45",
                "lower",
                "ocd-division/country:us/state:nh/sldl:hillsborough_45",
                1,
            ),
            District(
                "Merrimack 1",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_1",
                1,
            ),
            District(
                "Merrimack 2",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_2",
                1,
            ),
            District(
                "Merrimack 3",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_3",
                2,
            ),
            District(
                "Merrimack 4",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_4",
                2,
            ),
            District(
                "Merrimack 5",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_5",
                2,
            ),
            District(
                "Merrimack 6",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_6",
                1,
            ),
            District(
                "Merrimack 7",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_7",
                2,
            ),
            District(
                "Merrimack 8",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_8",
                3,
            ),
            District(
                "Merrimack 9",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_9",
                4,
            ),
            District(
                "Merrimack 10",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_10",
                4,
            ),
            District(
                "Merrimack 11",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_11",
                1,
            ),
            District(
                "Merrimack 12",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_12",
                2,
            ),
            District(
                "Merrimack 13",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_13",
                2,
            ),
            District(
                "Merrimack 14",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_14",
                1,
            ),
            District(
                "Merrimack 15",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_15",
                1,
            ),
            District(
                "Merrimack 16",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_16",
                1,
            ),
            District(
                "Merrimack 17",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_17",
                1,
            ),
            District(
                "Merrimack 18",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_18",
                1,
            ),
            District(
                "Merrimack 19",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_19",
                1,
            ),
            District(
                "Merrimack 20",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_20",
                1,
            ),
            District(
                "Merrimack 21",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_21",
                1,
            ),
            District(
                "Merrimack 22",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_22",
                1,
            ),
            District(
                "Merrimack 23",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_23",
                1,
            ),
            District(
                "Merrimack 24",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_24",
                1,
            ),
            District(
                "Merrimack 25",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_25",
                1,
            ),
            District(
                "Merrimack 26",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_26",
                1,
            ),
            District(
                "Merrimack 27",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_27",
                2,
            ),
            District(
                "Merrimack 28",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_28",
                1,
            ),
            District(
                "Merrimack 29",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_29",
                1,
            ),
            District(
                "Merrimack 30",
                "lower",
                "ocd-division/country:us/state:nh/sldl:merrimack_30",
                1,
            ),
            District(
                "Rockingham 1",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_1",
                3,
            ),
            District(
                "Rockingham 2",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_2",
                3,
            ),
            District(
                "Rockingham 3",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_3",
                1,
            ),
            District(
                "Rockingham 4",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_4",
                3,
            ),
            District(
                "Rockingham 5",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_5",
                2,
            ),
            District(
                "Rockingham 6",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_6",
                1,
            ),
            District(
                "Rockingham 7",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_7",
                1,
            ),
            District(
                "Rockingham 8",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_8",
                1,
            ),
            District(
                "Rockingham 9",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_9",
                2,
            ),
            District(
                "Rockingham 10",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_10",
                3,
            ),
            District(
                "Rockingham 11",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_11",
                4,
            ),
            District(
                "Rockingham 12",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_12",
                2,
            ),
            District(
                "Rockingham 13",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_13",
                10,
            ),
            District(
                "Rockingham 14",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_14",
                2,
            ),
            District(
                "Rockingham 15",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_15",
                2,
            ),
            District(
                "Rockingham 16",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_16",
                7,
            ),
            District(
                "Rockingham 17",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_17",
                4,
            ),
            District(
                "Rockingham 18",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_18",
                2,
            ),
            District(
                "Rockingham 19",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_19",
                1,
            ),
            District(
                "Rockingham 20",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_20",
                3,
            ),
            District(
                "Rockingham 21",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_21",
                1,
            ),
            District(
                "Rockingham 22",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_22",
                1,
            ),
            District(
                "Rockingham 23",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_23",
                1,
            ),
            District(
                "Rockingham 24",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_24",
                2,
            ),
            District(
                "Rockingham 25",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_25",
                9,
            ),
            District(
                "Rockingham 26",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_26",
                1,
            ),
            District(
                "Rockingham 27",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_27",
                1,
            ),
            District(
                "Rockingham 28",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_28",
                1,
            ),
            District(
                "Rockingham 29",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_29",
                4,
            ),
            District(
                "Rockingham 30",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_30",
                2,
            ),
            District(
                "Rockingham 31",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_31",
                2,
            ),
            District(
                "Rockingham 32",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_32",
                1,
            ),
            District(
                "Rockingham 33",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_33",
                1,
            ),
            District(
                "Rockingham 34",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_34",
                1,
            ),
            District(
                "Rockingham 35",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_35",
                1,
            ),
            District(
                "Rockingham 36",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_36",
                1,
            ),
            District(
                "Rockingham 37",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_37",
                1,
            ),
            District(
                "Rockingham 38",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_38",
                1,
            ),
            District(
                "Rockingham 39",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_39",
                1,
            ),
            District(
                "Rockingham 40",
                "lower",
                "ocd-division/country:us/state:nh/sldl:rockingham_40",
                1,
            ),
            District(
                "Strafford 1",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_1",
                2,
            ),
            District(
                "Strafford 2",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_2",
                3,
            ),
            District(
                "Strafford 3",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_3",
                1,
            ),
            District(
                "Strafford 4",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_4",
                3,
            ),
            District(
                "Strafford 5",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_5",
                1,
            ),
            District(
                "Strafford 6",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_6",
                1,
            ),
            District(
                "Strafford 7",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_7",
                1,
            ),
            District(
                "Strafford 8",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_8",
                1,
            ),
            District(
                "Strafford 9",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_9",
                1,
            ),
            District(
                "Strafford 10",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_10",
                4,
            ),
            District(
                "Strafford 11",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_11",
                3,
            ),
            District(
                "Strafford 12",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_12",
                4,
            ),
            District(
                "Strafford 13",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_13",
                1,
            ),
            District(
                "Strafford 14",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_14",
                1,
            ),
            District(
                "Strafford 15",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_15",
                1,
            ),
            District(
                "Strafford 16",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_16",
                1,
            ),
            District(
                "Strafford 17",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_17",
                1,
            ),
            District(
                "Strafford 18",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_18",
                1,
            ),
            District(
                "Strafford 19",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_19",
                3,
            ),
            District(
                "Strafford 20",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_20",
                1,
            ),
            District(
                "Strafford 21",
                "lower",
                "ocd-division/country:us/state:nh/sldl:strafford_21",
                3,
            ),
            District(
                "Sullivan 1",
                "lower",
                "ocd-division/country:us/state:nh/sldl:sullivan_1",
                1,
            ),
            District(
                "Sullivan 2",
                "lower",
                "ocd-division/country:us/state:nh/sldl:sullivan_2",
                1,
            ),
            District(
                "Sullivan 3",
                "lower",
                "ocd-division/country:us/state:nh/sldl:sullivan_3",
                3,
            ),
            District(
                "Sullivan 4",
                "lower",
                "ocd-division/country:us/state:nh/sldl:sullivan_4",
                1,
            ),
            District(
                "Sullivan 5",
                "lower",
                "ocd-division/country:us/state:nh/sldl:sullivan_5",
                1,
            ),
            District(
                "Sullivan 6",
                "lower",
                "ocd-division/country:us/state:nh/sldl:sullivan_6",
                3,
            ),
            District(
                "Sullivan 7",
                "lower",
                "ocd-division/country:us/state:nh/sldl:sullivan_7",
                1,
            ),
            District(
                "Sullivan 8",
                "lower",
                "ocd-division/country:us/state:nh/sldl:sullivan_8",
                2,
            ),
        ],
    ),
    upper=Chamber(
        chamber_type="upper",
        name="Senate",
        organization_id="ocd-organization/c95932a0-2ac1-4f14-a0c4-ade8568daac6",
        num_seats=24,
        title="Senator",
        districts=simple_numbered_districts(
            "ocd-division/country:us/state:nh", "upper", 24
        ),
    ),
)

#nesting
capitals={
    "France": "Paris",
    "Germany": "Berlin",
}

#nesting a list in a dictionary
travel_log={
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgard"],
}

#nesting dictionary in a dictionary
travel_Log2={
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgard"], "total_visited": 3}
}

#nesting dictionary in a list
travel_log3=[
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
        "total_visited": 3
    },
]
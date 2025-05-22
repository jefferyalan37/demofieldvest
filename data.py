# data.py

def get_projects():
    """
    Returns a list of dummy oil & gas projects.
    """
    return [
        {
            "id": "alpha",
            "name": "Alpha Well #123",
            "image_url": "https://via.placeholder.com/300x200.png?text=Alpha+Well+%23123",
            "target_irr": 0.25,
            "min_investment": 10000
        },
        {
            "id": "beta",
            "name": "Beta Drilling #456",
            "image_url": "https://via.placeholder.com/300x200.png?text=Beta+Drilling+%23456",
            "target_irr": 0.22,
            "min_investment": 20000
        },
        {
            "id": "gamma",
            "name": "Gamma Oil Field #789",
            "image_url": "https://via.placeholder.com/300x200.png?text=Gamma+Oil+Field+%23789",
            "target_irr": 0.30,
            "min_investment": 15000
        },
    ]


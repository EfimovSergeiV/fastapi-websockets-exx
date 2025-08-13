from random import randint


def gen_datasets(keyword):

    datasets = {
        "bar": [
            {
                "label": 'Значения',
                "backgroundColor": '#3b82f6',
                # "data": [10, 20, 15, 30, 25, 35, 40],
                "data": [randint(1, 100) for _ in range(7)]
            }
        ],
        "bubble": [
            {
                "label": 'Label 1',
                "data": [
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) }
                ],
                "backgroundColor": 'rgba(255, 99, 132, 0.5)'
            },
            {
                "label": 'Label 2',
                "data": [
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) },
                    { "x": randint(1, 100), "y": randint(1, 100), "r": randint(1, 30) }
                ],
                "backgroundColor": 'rgba(54, 162, 235, 0.5)'
            }
        ],
        "multiline": [
            {
                "label": 'Dataset 1 (Левая ось)',
                "data": [randint(1, 500) for _ in range(7)],
                "borderColor": 'rgb(255, 99, 132)',
                "backgroundColor": 'rgba(255, 99, 132, 0.5)',
                "yAxisID": 'y',
            },
            {
                "label": 'Dataset 2 (Правая ось)',
                "data": [randint(1, 500) for _ in range(7)],
                "borderColor": 'rgb(54, 162, 235)',
                "backgroundColor": 'rgba(54, 162, 235, 0.5)',
                "yAxisID": 'y',
            }
            ]

    }
    return datasets.get(keyword, [])
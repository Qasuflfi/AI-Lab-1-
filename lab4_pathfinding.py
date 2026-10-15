# Lab 4: Intelligent Pathfinding Using A* and Uniform Cost Search

routes = {
    'Start': [('A', 2), ('B', 5)],
    'A': [('C', 2)],
    'B': [('Goal', 3)],
    'C': [('Goal', 2)],
    'Goal': []
}

estimated_distance = {
    'Start': 6,
    'A': 4,
    'B': 3,
    'C': 2,
    'Goal': 0
}


def calculate_path_cost(path):
    total_cost = 0
    for current, following in zip(path, path[1:]):
        for neighbor, travel_cost in routes[current]:
            if neighbor == following:
                total_cost += travel_cost
                break
        else:
            raise ValueError(f'No route from {current} to {following}')
    return total_cost


def astar_search(start, destination, heuristic):
    frontier = [(start, [start], 0)]
    while frontier:
        frontier.sort(key=lambda item: item[2] + heuristic[item[0]])
        current, path, cost_so_far = frontier.pop(0)
        if current == destination:
            return path, cost_so_far
        for neighbor, step_cost in routes[current]:
            if neighbor not in path:
                frontier.append((neighbor, path + [neighbor], cost_so_far + step_cost))
    return None


def uniform_cost_search(start, destination):
    frontier = [(start, [start], 0)]
    while frontier:
        frontier.sort(key=lambda item: item[2])
        current, path, cost_so_far = frontier.pop(0)
        if current == destination:
            return path, cost_so_far
        for neighbor, step_cost in routes[current]:
            if neighbor not in path:
                frontier.append((neighbor, path + [neighbor], cost_so_far + step_cost))
    return None


def show_result(title, result):
    print('\n' + title)
    if result is None:
        print('No path found')
        return
    path, cost = result
    print('Path:', ' -> '.join(path))
    print('Total cost:', cost)
    print('Verified cost:', calculate_path_cost(path))


if __name__ == '__main__':
    show_result('A* Search', astar_search('Start', 'Goal', estimated_distance))
    show_result('Uniform Cost Search', uniform_cost_search('Start', 'Goal'))

    changed_heuristic = estimated_distance.copy()
    changed_heuristic['C'] = 10
    print('\nHeuristic Experiment')
    print('Original estimate for C:', estimated_distance['C'])
    print('Changed estimate for C:', changed_heuristic['C'])
    show_result('A* With Changed Heuristic', astar_search('Start', 'Goal', changed_heuristic))
    print('\nAn overestimated heuristic can make A* choose a more expensive path.')

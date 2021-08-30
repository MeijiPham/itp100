def plurality(election):
    """
    Return the plurality winner among three candidates, 1, 2, and 3. The input
    election is a list of three tuples, so in a plurality election only the
    first element matters.

      >>> plurality([(1, 2, 3), (2, 3, 1), (2, 1, 3)])
      2
      >>> plurality([(3, 2, 1), (3, 2, 1), (2, 1, 3)])
      3
    """
    # Count the votes for each of the three candidates in a dictionary
    vote_totals = {1: 0, 2: 0, 3: 0} 
    for vote in election:
        vote_totals[vote[0]] += 1

    # Return the candidate number with the highest vote count
    return max(vote_totals.items(), key=lambda x: x[1])[0]

def exhaustive(election):
    """
    Similar to plurality winner but there will be two elections. Find the losing candidate
    in the first election then make sure their vote isn't counted for the second.

      >>> exhaustive([(1, 2, 3), (1, 3, 2), (2, 3, 1)])
      1
      >>> exhaustive([(2, 3, 1), (2, 1, 3), (2, 1, 3), (1, 3, 2)])
      2
    """
    # First election
    vote_totals = {1: 0, 2: 0, 3: 0} 
    for vote in election:
        vote_totals[vote[0]] += 1

    losing_candidate = min(vote_totals.items(), key=lambda x: x[1])[0]

    # Second election
    vote_totals = {1: 0, 2: 0, 3: 0} 
    for vote in election:
        for i in vote:
            if i == losing_candidate:
                continue
            vote_totals[i] += 1
            break
    
    return max(vote_totals.items(), key=lambda x: x[1])[0]

def primary(election, first_can_num, second_can_num):
    """
    Return winner of first election and eliminate the loser. Then compare winner with
    remaining candidate.

      >>> primary([(3, 2, 1), (3, 2, 1), (2, 1, 3)], 1, 2)
      3
      >>> primary([(1, 3, 2), (1, 2, 3), (3, 2, 1)], 1, 3)
      1
      >>> primary([(1, 2, 3), (2, 3, 1), (2, 1, 3)], 2, 3)
      2
    """
    # First election
    first_candidates = [first_can_num, second_can_num]
    vote_totals = {1: 0, 2: 0, 3: 0}
    for vote in election:
        for i in vote:
            if i not in first_candidates:
                continue
            vote_totals[i] += 1
            break
    winning_candidate = max(vote_totals.items(), key=lambda x: x[1])[0]

    # Finalists
    second_candidates = [1, 2, 3]
    second_candidates = [x for x in second_candidates if x not in first_candidates]
    second_candidates.append(winning_candidate)

    # Second election
    vote_totals = {1: 0, 2: 0, 3: 0}
    for vote in election:
        for i in vote:
            if i not in second_candidates:
                continue
            vote_totals[i] += 1
            break

    return max(vote_totals.items(), key=lambda x: x[1])[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

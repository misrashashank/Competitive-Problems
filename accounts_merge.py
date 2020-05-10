'''
Given a list accounts, each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some email
that is common to both accounts. Note that even if two accounts have
the same name, they may belong to different people as people could have
the same name. A person can have any number of accounts initially,
but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format:
the first element of each account is the name,
and the rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.

Example 1:

Input: 
accounts =
[["John", "johnsmith@mail.com", "john00@mail.com"],
["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"],
["Mary", "mary@mail.com"]]

Output:
[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
["John", "johnnybravo@mail.com"],
["Mary", "mary@mail.com"]]

Explanation: 
The first and third John's are the same person as they have
the common email "johnsmith@mail.com".
The second John and Mary are different people as none of
their email addresses are used by other accounts.
We could return these lists in any order, for example the answer

[['Mary', 'mary@mail.com'],
['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
would still be accepted.

Note:
The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
'''


from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts:):
        '''
        Array > Array
        
        Build graph (adjacency list)
        Traverse over it using DFS to find all emails
        '''
        
        # Build adjacency list
        adj_list = collections.defaultdict(set)
        email_to_name = {}
        for account in accounts:
            for email in account[1:]:
                
                # Undirected graph, hence, adding node both ways
                adj_list[account[1]].add(email)
                adj_list[email].add(account[1])
                
                # To keep track of name associated with the email
                email_to_name[email] = account[0]
        
        # Traverse adjacency list to find connected components
        visited = set()
        result = []
        
        for email in adj_list:
            if email not in visited:
                visited.add(email)
                
                # Stack for DFS
                stack = [email]
                
                # Connected components
                connected_components = []
                
                while(stack):
                    current_node = stack.pop()
                    connected_components.append(current_node)
                    
                    # Check for nodes connected with current_node
                    for neighbor in adj_list[current_node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                
                # When whole connected component has been traversed
                new_merged_account = [email_to_name[connected_components[0]]] + sorted(connected_components)
                result.append(new_merged_account)
        
        return result

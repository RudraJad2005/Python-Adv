# Sometimes you'll want to accept an arbitrary number of arguments, but you won't know ahead of time what kind of informationn will be passed to the function. 
# In this case, you can write functions that accept as many key-value pairs  as the calling statement provides. Below is an example for it.

# ... The definition of bulding_profile()vexcepts a first and last name, and then it allows the user to pass in as many name-value paird as they want.

def build_profile(first, last, **user_info):

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
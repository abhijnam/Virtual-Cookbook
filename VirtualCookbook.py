# Most people have a hard time deciding what to eat for breakfast and Lunch , especially sleep deprived university students, so this program gives them the option to pick out different reciepes to make one by one. This is better than a website since they won't be overwhelmed by choice and gives a choice to everyon's eating choices(ex: if someone is vegan or if someone is vegetarian)
 #introduction
def intro():
    print("Welcome to your own cook book :)") 
    # print statement to ask the user what they need to input
    print("To customize your options select one of the following below")
    # print statement to show the user the different meal options they have  
    print("\n1.Breakfast\n2.Lunch")
    # the input that is needed and begins our code since it stores the user input into the object we have assigned it to
    user_input = int(input("\nEnter option:"))
    easyCook(user_input)
    
def easyCook(user_input):#defined my fuctions as easyCook and left the argument blank since I am using user-inputs for my program
    # This while loop is to print out the series of steps that will take the user where they want to be i.e to show them the selection of reciepes
    while user_input == 1 : 
         # an introductory sentence to inform the user that they will now see a selection from easy breakfast meals
        print("Thank you for your input, your will now get a selection of recipes from easy breakfast meals") 
        # prints out the first recipe on a new line
        print("\n Recipe #1")
        # prints out the name of the recipe on a new line
        print("\n: Ham and Swiss Omelet :")
        # prints out the first reciepe ingredies
        print("\n Ingredients \n1. 1 tablespoon butter\n2. 3 eggs\n3. 3 tablespoons water\n4. 1/8 teaspoon salt\n5. 1/8 teaspoon pepper\n6. 1/2 cup cubed fully cooked ham\n7. 1/4 cup shredded Swiss cheese") 
        # prints out the directions for first reciepe
        print("\n Directions \n1. In a small nonstick skillet, melt butter over medium-high heat. Whisk the eggs, water, salt and pepper. Add egg mixture to skillet (mixture should set immediately at edges).\n2. As eggs set, push cooked edges toward the center, letting uncooked portion flow underneath. When the eggs are set, place ham on one side and sprinkle with cheese; fold other side over filling. Slide omelet onto a plate.")
        # asks the user if they would like to continue viewing the reciepes or if they would like to exit (if they already found a recipe that they liked, they can exit out of the program)
        print("\n Would you like to see more recipes from easy breakfast meals? ")
        #This is to store the response of the breakfast input by the user for the print statement qiven on line 14
        response_breakfast = input("Enter yes or no:")
        #compared the response to see if it matches as true
        if response_breakfast == "yes": 
             #prints out the second recipe on a new line
            print("\n Recipe #2")
            #prints out the name of the recipe on a new line
            print("\n: Fruity Waffle Parfaits :")
            #prints the ingredients of the reciep given above
            print("\n Ingredients\n1. 4 frozen low-fat multigrain waffles\n2. 1/2 cup almond butter or creamy peanut buttercups\n3. strawberry yogurt\n4. 2 large bananas, sliced\n5. 2 cups sliced fresh strawberries\n6. Toasted chopped almonds, optional\n7. Maple syrup, optional")
            #prints out the directions to follow 
            print("\n Directions\n1. Toast waffles according to package directions. Spread each waffle with 2 tablespoons almond butter.\n2. Cut waffles into bite-sized pieces.Layer half the yogurt, bananas, strawberries and waffle pieces into 4 parfait glasses. Repeat layers.\n3. If desired, top with toasted almonds and maple syrup. Serve immediately.")
            #prints out the third reciepe on a new line
            print("\n Recipe #3")
            #prints out the name of the recipe on a new line
            print("\n: Eggs & Chorizo Wraps :")
            #prints out the ingredients of the recipe given about
            print("\n Ingredients\n1. 12 ounces fresh chorizo\n2. 6 large eggs\n3. 2 tablespoons 2% milk\n4. 1 cup shredded cheddar cheese\n5. 6 flour tortillas (8 inches), warmed\n Optional toppings: Thinly sliced green onions, minced fresh cilantro and salsa")
            #prints out the directions to follow
            print("\n Directions\n1. Remove chorizo from casings.\n2. In a large cast-iron or other heavy skillet, cook chorizo over medium heat until cooked through, breaking into crumbles, 6-8 minutes.\n3. Drain and return to pan.In a small bowl, whisk eggs and milk until blended.\n4. Add egg mixture to chorizo. Cook and stir until eggs are thickened and no liquid egg remains.\n Stir in cheese. Spoon 1/2 cup egg mixture across center of each tortilla.\n5. Add toppings of your choice. Fold bottom and sides of tortilla over filling and roll up.")
            response_breakfast_second_while = input("\n Do you want to continue or exit (C/E):")
            n = 0#we have assign a value to a variable
            while n < 4:#the while loop will repeat 3 times before ending
                if response_breakfast_second_while == "c" or "C":
                    # asks what reciepe the user would like to view
                    print("\n what recipe number would you like to view between 4-6 or hit 1 to exit")
                    #gives important details about each recipe
                    print("\n Note \n 4| is a healthy vegetarian option \n 5| kick it back old school and option \n 6| vegan option ")
                    # input to start the if statement for the options the user gets above
                    response_breakfast_of_hab =input("Enter number:")
                    #Condition to compare the response of the user 
                    if response_breakfast_of_hab == "4":
                        #prints out fourth reciepe
                        print("\n Recipe #4")
                        #prints out the name of the 4th recipe
                        print("\n: Breakfast Sweet Potatoes :")
                        #prints of the ingredients needed
                        print("\n Ingredients\n1. 4 medium sweet potatoes (about 8 ounces each)\n2. 1/2 cup fat-free coconut Greek yogurt\n3. 1 medium apple, chopped\n4. 2 tablespoons maple syrup\n5. 1/4 cup toasted unsweetened coconut flakes")
                        #prints out the directions to follow
                        print("\n Directions\n 1. Preheat oven to 400°. Place potatoes on a foil-lined baking sheet\n 2. Bake until tender, 45-60 minutes\n 3. With a sharp knife, cut an X in each potato. Fluff pulp with a fork. Top with remaining ingredients.")
                    #condition to compare the option if the above if statement was false
                    elif response_breakfast_of_hab == "5":
                        #prints out 5th recipe
                        print("\n Recipe #5 ")
                        #prints out the name of the reciepe
                        print("\n: Waffle Sandwich :")
                        #prints out the ingredients
                        print("\n Ingredients\n1. 1 slice Canadian bacon\n1 large egg\n2. 1 green onion, chopped\n3. 2 frozen low-fat multigrain waffles\n4. 1 tablespoon shredded reduced-fat cheddar cheese\n5. Sliced tomato, optional ")
                        #prints out the directions to follow
                        print("\n Directions\n1. In a nonstick skillet, cook Canadian bacon over medium-high heat 1-2 minutes on each side or until lightly browned. Remove and keep warm.\n2. In a small bowl, whisk egg and green onion; add to the same pan. Cook and stir until egg is thickened and no liquid egg remains.\n3. Meanwhile, prepare waffles according to package directions. Place 1 waffle on a plate. Top with Canadian bacon, scrambled egg, cheese and, if desired, tomato. Top with remaining waffle.")
                    #condition to compare the option if the above elif condition wasn't met
                    elif response_breakfast_of_hab == "6":
                        #prints the sixth reciepe
                        print("\n Recipe #6")
                        #prints out the name of the reciepe
                        print("\n: Banana Oatmeal Pancakes :")
                        #prints out the ingredients 
                        print("\n Ingredients\n1. 2 cups complete whole wheat pancake mix\n2. 1 large firm banana, finely chopped\n3. 1/2 cup old-fashioned oats\n1/4 cup chopped walnuts")
                        #prints out the directions
                        print("\n Directions\n1. Prepare pancake batter according to package directions. Stir in the banana, oats and walnuts. Pour batter by 1/4 cupfuls onto a hot griddle coated with cooking spray; turn when bubbles form on top. Cook until the second side is golden brown.")
                    elif response_breakfast_of_hab == "1":
                        break
                n = n + 1
            if response_breakfast_second_while =="e" or "E":
                print("Thank you for visiting")
        # boolean operator (==) and if  to create a statement that will be printed after the user enters their response
        if response_breakfast == "no": 
                #end response after the user enters exit or no to
            print("Thank you for visiting")
    # updates the value of the user input to end the while loop
        user_input += 4

    while user_input == 2 :
        print("Thank you for yout input, you will now get a selection of reciepes from easy Lunch meals")
        print("\n Recipe #1")
        print("\n: Microwave 3-minute Omelette In A Mug :")
        print("\n Ingredients \n1. 2 eggs\n2. 1/2 bell pepper, diced\n3. 2 slices ham, diced\n4. 1/4 cup fresh spinach(10 g) chopped \n5. add salt and pepper to your liking" )
        print("\n Directions \n1. Combine all ingredients in a microwaveable mug\nCook for 2-3 minutes, making sure the egg doesn't bubble over. Stir halfway through the cooking process.\n Enjoy!")
        print("\n Would you like to see more recipes from easy Lunch meals? ")
        response_lunch = input("Enter yes or no:")
            
        if response_lunch == "yes":
            print("\n Recipe #2")
            print("\n: Microwave 10-minute Loaded Potato :")
            print("\n Ingredients\n1. 1 russet potato, washed and scrubbed\n2. 1 tablespoon oil\n3. salt, to taste\n4. 2 slices bacon\n5. ¼ cup shredded cheddar cheese(25 g)\n6. sour cream, to serve\n7. fresh chive, to serve ")
            print("\n Directions\n1. Poke holes in the potato with a fork, then rub with oil and salt.\n2. Place the bacon slices on the same plate as the potato, microwave for 7-9 minutes until the bacon is crispy and the potato is tender. Make sure the bacon does not burn.\n3. Crumble the bacon after it’s cooled down.\n4. Slice the potato in half, then use a fork to fluff up the insides.\n5. Sprinkle the cheese on top, then microwave for another 30 seconds.\n6. Top with sour cream, the crushed bacon bits, and the chives.\nEnjoy! ")
            print("\n Recipe #3")
            print("\n: 3-ingredient creamy rotisserie chicken salad :")
            print("\n Ingredients\n1. 2 cups chopped rotisserie chicken\n2. 3/4 cup chopped celery\n3. 1/3 cup lemon-herb-flavored mayonnaise\n4. Cracked black pepper ")
            print("\n Directions\n1. Combine chicken and celery in a medium bowl. Fold in mayonnaise and mix well to combine. Season with pepper. ")
            response_lunch_second_while = input("\n Do you want to continue or exit(C/E):")
            n = 0
            while n < 4:
                if response_lunch_second_while == "c" or "C":
                    print("\n what recipe number would you like to view between 4-6 or hit 1 to exit")
                    print("\n Note \n 4| is a vegan option \n 5|kick it back old school and option \n 6|vegetarian option ")
                    response_lunch_2=input("Enter number:")
                    if response_lunch_2 == "4":
                        print("\n Recipe #4")
                        print("\n: Chickpea Sandwich Filling :")
                        print("\n Ingredients\n1. 1 can chickpeas drained\n2. 1/3 cup aquafaba or vegan mayo*\n3. 1/2 teaspoon turmeric\n4. 1/2 teaspoon onion powder\n5. 1 clove garlic minced\n black pepper to taste\n6. salt to tast")
                        print("\n Directions\n1. Pulse all ingredients in a blender until well-incorporated and broken down, but not totally mushy. You still want some texture in there")
                    elif response_lunch_2 == "5":
                        print("\n Recipe #5 ")
                        print("\n: Creamy Pasta :")
                        print("\n Ingredients\n1. 800ml vegetable stock\n2. 250g linguine pasta\n3. 1 onion, sliced\n4. 1/2 broccoli, broken into florets\n5. 250 (Approx. 8 rashers) bacon, chopped\n6. 150g peas\n7. 1 Clove garlic, crushed\n 40g Perfect Italiano Parmesan, shave")
                        print("\n Directions\n1. In a large heavy pot add all ingredients except the Perfect Italiano Parmesan\n2. Bring to the boil, once boiling begin tossing for 7 -8 minutes, add parmesan and continue cooking for another 1-2 minutes until the pasta and vegetables are tender\n3. Let pasta sit for a couple of minutes before serving, allowing pasta to soak the excess stock in the pot\n Season, then top with any remaining Perfect Italiano Shaved Parmesan and serve")
                    elif response_lunch_2 == "6":
                        print("\n Recipe #6")
                        print("\n: Black bean burrito :")
                        print("\n Ingredients\n1. 1 tablespoon canola oil\n2. 3 tablespoons chopped onion\n3. 3 tablespoons chopped green pepper\n4. 1 can (15 ounces) black beans, rinsed and drained\n5. 4 flour tortillas (8 inches), warmed\n6. 1 cup shredded Mexican cheese blend\n7. 1 medium tomato, chopped\n 1 cup shredded lettuce\n8. Optional toppings: Salsa, sour cream, minced fresh cilantro and cubed avocado")
                        print("\n Directions\n1. In a nonstick skillet, heat oil over medium heat; saute onion and green pepper until tender.\n2. Stir in beans; heat through.\n3. Spoon about 1/2 cup of vegetable mixture off-center on each tortilla. Sprinkle with the cheese, tomato and lettuce.\n4. Fold sides and ends over filling and roll up. Serve with optional toppings as desired.")
                    elif response_lunch_2 == "1":
                        break
                n = n + 1
            if response_lunch_second_while =="e" or "E":
                    print("Thank you for visiting")
        if response_lunch == "no":
            print("Thank you")
        user_input += 2
def exit():
    input_response = input("would you like to exit completely yes or no:")
    if input_response == "yes":
        print("Thank you for visiting")
    return input_response


if __name__ == "__main__":
    complete_exit = ''
    while complete_exit != "yes":
        intro()
        complete_exit = exit()
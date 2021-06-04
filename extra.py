import random

quoteLs = ['Believe you can and you’re halfway there.',
        'You have to expect things of yourself before you can do them.',
        'It always seems impossible until it’s done.',
        'Don’t let what you cannot do interfere with what you can do.',
        'Start where you are. Use what you have. Do what you can.',
        'Successful and unsuccessful people do not vary greatly in their abilities. They vary in their desires to reach their potential.',
        'The secret of success is to do the common things uncommonly well.',
        'Good things come to people who wait, but better things come to those who go out and get them.',
        'Strive for progress, not perfection.',
        'I find that the harder I work, the more luck I seem to have.',
        'The secret to getting ahead is getting started.',
        'You don’t have to be great to start, but you have to start to be great.',
        'The expert in everything was once a beginner.',
        'There are no shortcuts to any place worth going. ',
        'Push yourself, because no one else is going to do it for you.',
        'Some people dream of accomplishing great things. Others stay awake and make it happen.',
        'There is no substitute for hard work.',
        'The difference between ordinary and extraordinary is that little “extra.”',
        'You don’t always get what you wish for; you get what you work for.',
        'It’s not about how bad you want it. It’s about how hard you’re willing to work for it.',
        'The only place where success comes before work is in the dictionary.',
        'If people only knew how hard I’ve worked to gain my mastery, it wouldn’t seem so wonderful at all.',
        'If it’s important to you, you’ll find a way. If not, you’ll find an excuse.',
        'Don’t say you don’t have enough time. You have exactly the same number of hours per day that were given to Helen Keller, Pasteur, Michelangelo, Mother Teresea, Leonardo da Vinci, Thomas Jefferson, and Albert Einstein.',
        'Challenges are what make life interesting. Overcoming them is what makes life meaningful.',
        'Life has two rules: 1) Never quit. 2) Always remember Rule #1.',
        'I don’t measure a man’s success by how high he climbs, but how high he bounces when he hits the bottom.',
        'Don’t let your victories go to your head, or your failures go to your heart.',
        'You don’t drown by falling in the water; you drown by staying there.',
        'The difference between a stumbling block and a stepping-stone is how high you raise your foot.',
        'The pain you feel today is the strength you will feel tomorrow. For every challenge encountered there is opportunity for growth.'
        ]
def chooseQuote():
  return random.choice(quoteLs)

def playDice(player1, player2):
  numLs = [1,2,3,4,5,6]
  num1 = random.choice(numLs)
  num2 = random.choice(numLs)
  if num1 < num2:
    result = player1 + " : " + num1 + "\n" + player2 + " : " + num2 + "\nWinner: " + player2
  elif num1 > num2:
    result = player1 + " : " + num1 + "\n" + player2 + " : " + num2 + "\nWinner: " + player1
  else:
    result = "It's a draw!"
  return result
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Level 1 Game : Rock, Paper , Scissors"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# with this program the user will be playing  against te computer.\n",
    "# before playing the players will make the following statement.  \n",
    "\n",
    "import  random\n",
    "\n",
    "user_wins = 0\n",
    "compt_wins =0\n",
    "\n",
    "def choice():\n",
    "    user_choice = input( \"choose rock , paper or scissors:\")\n",
    "    if user_choice in [\" Rock\", \"rock\",\"r\",\"R\"]:\n",
    "        user_choice = \"r\"\n",
    "    elif user_choice in [\"paper\",\"Paper\",\"p\",\"P\"]:\n",
    "        user_choise = \"p\"\n",
    "    elif user_choice in[\"Scissors\", \"scissors\", \"s\",\"S\"]:\n",
    "        user_choise = \"s\"\n",
    "        \n",
    "    else :\n",
    "        print(\"answer does not match please try again\")\n",
    "        choice()\n",
    "    return user_choice\n",
    "    \n",
    "def computer():\n",
    "    compt_choice = random.randint(1,3)\n",
    "    if compt_choice == 1:\n",
    "        compt_choice = \"r\"\n",
    "    elif compt_choice == 2:\n",
    "        compt_choice = \"P\"\n",
    "    else :\n",
    "        compt_choice = \"s\"\n",
    "    return compt_choice \n",
    "\n",
    "while True :\n",
    "    print(\" \")\n",
    "    user_choice = choice ()\n",
    "    compt_choice = computer ()\n",
    "    print(\" \")\n",
    "    \n",
    "if user_choice == \"r\":\n",
    "    if compt_choice == \"r\":\n",
    "        print(\"is a tie\")\n",
    "    elif compt_choice == \" p\":\n",
    "        print( \"you lost \")\n",
    "        compt_wins += 1\n",
    "        \n",
    "    elif compt_choice == \"s\":\n",
    "        print( \"you win\")\n",
    "        user_wins +=1\n",
    "    \n",
    "elif user_choice == \"p\":\n",
    "    if compt_choice == \"p\":\n",
    "        print(\"is a tie\")\n",
    "    elif compt_choice == \" r\":\n",
    "        print( \"you lost \")\n",
    "        compt_wins += 1\n",
    "        \n",
    "    elif compt_choice == \"s\":\n",
    "        print( \"you win\")\n",
    "        user_wins +=1   \n",
    "        \n",
    "elif user_choice == \"S\":\n",
    "    if compt_choice == \" s\":\n",
    "        print(\"you tie\")\n",
    "\n",
    "    elif compt_choice == \"p\":\n",
    "        print(\" you win\")\n",
    "        user_wins += 1\n",
    "        \n",
    "    elif compt_choice ==\"r\":\n",
    "        print( \" you lost\")\n",
    "        compt_wins += 1\n",
    "        \n",
    "print(\"\") \n",
    "print(\" user wins: \") + str(user_wins )\n",
    "print( \" computer wins: \") + str(compt_wins)\n",
    "print(\" \")\n",
    "\n",
    "user_choice = input( \" do you want to keep playing? (y/n)\")\n",
    "if user_choice in [\"Y\",\"y\",\"yes\",\"Yes\"]:\n",
    "    pass\n",
    "elif user_choice in [\"N\", \"n\", \"no\", \"No\"]:\n",
    "    return\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

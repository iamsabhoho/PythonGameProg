{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter your test grade(0-100): 80\n",
      "Your test grade is B-\n"
     ]
    }
   ],
   "source": [
    "TestGrade = int(input('Please enter your test grade(0-100): '))\n",
    "\n",
    "\n",
    "if 97 <= TestGrade <= 100:\n",
    "    print('Your test grade is A+')\n",
    "elif 93 <= TestGrade <= 96:\n",
    "    print('Your test grade is A')\n",
    "elif 90 <= TestGrade <= 92:\n",
    "    print('Your test grade is A-')\n",
    "    \n",
    "elif 87 <= TestGrade <= 89:\n",
    "    print('Your test grade is B+')\n",
    "elif 83 <= TestGrade <= 86:\n",
    "    print('Your test grade is B')\n",
    "elif 80 <= TestGrade <= 82:\n",
    "    print('Your test grade is B-')\n",
    "    \n",
    "elif 77 <= TestGrade <= 79:\n",
    "    print('Your test grade is C+')\n",
    "elif 73 <= TestGrade <= 76:\n",
    "    print('Your test grade is C')\n",
    "elif 70 <= TestGrade <= 72:\n",
    "    print('Your test grade is C-')\n",
    "\n",
    "elif 67 <= TestGrade <= 69:\n",
    "    print('Your test grade is D+')\n",
    "elif 63 <= TestGrade <= 66:\n",
    "    print('Your test grade is D')\n",
    "elif 60 <= TestGrade <= 62:\n",
    "    print('Your test grade is D-')\n",
    "\n",
    "elif 0 <= TestGrade <=59: \n",
    "    print('You failed. F.')\n",
    "else:\n",
    "    print('Not a valid test grade.')"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}

#
# TO IMPLEMENT
# 
import expense_tracker
import argparse

args = argparse.Namespace(description="New expense", amount=50)

for i in range(20):
    expense_tracker.add(args)

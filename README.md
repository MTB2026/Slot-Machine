Python Slot Machine
A terminal-based slot machine game written in Python. Manage your bank, place bets, spin the reels, and try to hit the jackpot, without going broke.
-----------------------------------------------------
Features
-----------------------------------------------------
Configurable spins and bet amount per round
Running bank balance with win/loss tracking
Loan system to keep playing when funds run low
Multiple winning combinations with different multipliers
Consolation prize for two-of-a-kind matches
Debt tracking with automatic repayment from winnings
Bankruptcy detection — game ends if you're broke and in debt
Emoji slot symbols for a visual experience
-----------------------------------------------------
How to Play
-----------------------------------------------------
Check your balance — you start with £1000.
Choose your spins — how many times the reels will spin this round.
Place your bet — the amount wagered per spin.
Can't afford it? — you'll be offered a loan, which adds to your debt.
Spin — the reels land on one of 7 symbols per slot.
Winnings — are calculated automatically and used to pay off debt first, then added to your bank.
Keep going or cash out — after each round you decide whether to continue.
-----------------------------------------------------
Loan & Debt System
-----------------------------------------------------
If your total bet exceeds your bank balance, you'll be offered a loan.
The loan amount is added to your debt counter.
Any winnings automatically repay your debt before being credited to your bank.
If you finish a round still in debt, a warning is displayed.
If your bank hits £0 or below while you're in debt, the game ends.
-----------------------------------------------------

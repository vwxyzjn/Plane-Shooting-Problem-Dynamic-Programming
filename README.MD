# The Plane Shooting Problem (Dynamic Programming)
Costa Huang
This is a problem in my *Information Structure* class in Fuman University taught by Dr. Chris Healy

## Introduction

The nation is at war. The enemy send out a squadron of $n$ planes to attack our troops from various angles. You have a very precise anti-aircraft launcher that will be used to shoot enemy planes. If the launcher is aimed directly at an enemy plane, it's guaranteed to destroy the plane. Unfortunately, your launcher is ponderous to reposition. Namely, you can only move 1 degree per minute. Then 1 plane enter your shoot range per minute. Once they go passed your shoot range, they are gone and you can't shoot them again. You are tasked to destroy the first plane, and then destroy as many plane as possible. 

## Examples

The plane is coming at [50,49,60,48,54,55,56,57,58] angles for each minute. You shoot down the first plane at 50 degree and you can either statys at 50 degree, move to 51 degree, or move to 49 degree. The optimal solution would be shooting down 6 aircraft: [50,54,55,56,57,58].

## Analysis

Notice this problem can be solved by brute force method. For each position, we can either statys at $k$ degree, move to $k+1$ degree, or move to $k-1$ degree. So we can just try all possible possibilities and see which possibility shoot the most plane. We therefore demonstrate a brute force approach:
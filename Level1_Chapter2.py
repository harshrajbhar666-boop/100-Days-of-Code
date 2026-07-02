# Conditional Statements (if-elif-else)


print("--- Range Function ---")
for i in range(2, 11, 2):
    print(f"Number: {i}")


print("\n--- Enumerate Function ---")
skills = ["Python", "Machine Learning", "Communication"]
for index, skill in enumerate(skills, start=1):
    print(f"Skill {index}: {skill}")


print("\n--- Zip Function ---")
projects = ["Saathi AI", "Project Hive", "E.V.A."]
tech = ["Python", "Modular Robotics", "AI Agents"]

for proj, tk in zip(projects, tech):
    print(f"🚀 {proj} ban raha hai {tk} ka use karke.")


# Control Statements

print("n\---Brake vs continue vs pass---")

print("Testing continue(3 skip hoga:)")
for step in range(1,6):
    if step==3:
        continue
    print(f"Step {step} complete.")

print("n\ Testing Break (4 par loop khatam)")
for step in range(1,6):
    if step==4:
        print("Limit break ho raha hai ")
        break
    print(f"Processing step {step}")

print("\n Testing Pass:")
for step in range(1, 3):
    pass 
print("Pass successfully executed!") 

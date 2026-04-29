import json
from main import classify_email

# Load test cases
with open("test_cases.json", "r") as f:
    test_cases = json.load(f)

correct = 0
total = len(test_cases)

error_cases = []

print("\n📊 EVALUATION STARTED...\n")

for i, case in enumerate(test_cases, 1):
    print(f"Test Case {i}")

    output = classify_email(case["input"])

    predicted = output.get("intent")
    expected = case["expected_intent"]

    # ✅ Normalize null/None handling
    if predicted == "null":
        predicted = None

    # ✅ Compare safely
    is_correct = (predicted == expected) or (predicted is None and expected is None)

    if is_correct:
        correct += 1
    else:
        error_cases.append({
            "input": case["input"],
            "expected": expected,
            "predicted": predicted,
            "full_output": output
        })

    print(f"Input: {case['input']}")
    print(f"Expected: {expected}")
    print(f"Predicted: {predicted}")
    print(f"Result: {'✅ Correct' if is_correct else '❌ Incorrect'}")
    print("-" * 50)

# Accuracy
accuracy = correct / total * 100

print("\n==============================")
print(f"✅ Accuracy: {accuracy:.2f}%")
print("==============================\n")

# Show failure cases
if error_cases:
    print("⚠️ FAILURE CASES:\n")
    for err in error_cases:
        print(f"Input: {err['input']}")
        print(f"Expected: {err['expected']} | Predicted: {err['predicted']}")
        print("Full Output:")
        print(json.dumps(err["full_output"], indent=2, ensure_ascii=False))
        print("-" * 50)
else:
    print("🎉 No failure cases! (Still mention limitations in README)")
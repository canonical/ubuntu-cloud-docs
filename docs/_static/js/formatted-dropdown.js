document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".dropdown-widget").forEach(widget => {
        const format = widget.dataset.format;
        const options = JSON.parse(widget.dataset.options);

        const selects = widget.querySelectorAll(".dropdown-select");
        const output = widget.querySelector(".dropdown-output-text");
        const copyBtn = widget.querySelector(".dropdown-copy");

        // Full option map for recomputation
        const fullOptions = {};
        for (const key in options) {
            fullOptions[key] = options[key].map(o => ({...o}));
        }

        function computeAvailableValues(key) {
            const deps = fullOptions[key];

            const current = {};
            selects.forEach(sel => {
                current[sel.dataset.key] = sel.value;
            });

            return deps.filter(item => {
                for (const condKey in item.conditions) {
                    const allowedVals = item.conditions[condKey];
                    if (!allowedVals.includes(current[condKey])) {
                        return false;
                    }
                }
                return true;
            });
        }

        function updateDropdowns() {
            selects.forEach(sel => {
                const key = sel.dataset.key;
                const field = widget.querySelector(`.dropdown-field[data-field="${key}"]`);

                const prevValue = sel.value;
                const available = computeAvailableValues(key);

                sel.innerHTML = available
                    .map(o => `<option value="${o.value}">${o.value}</option>`)
                    .join("");

                // Try to restore previous value
                if (available.some(a => a.value === prevValue)) {
                    sel.value = prevValue;
                } else {
                    // Otherwise pick first valid value
                    sel.value = available[0]?.value;
                }

                // Hide the field if only one possible value
                if (available.length === 1) {
                    field.style.display = "none";
                } else {
                    field.style.display = "flex";
                }
            });
        }

        function updateOutput() {
            let result = format;
            selects.forEach(sel => {
                result = result.replace(`{${sel.dataset.key}}`, sel.value);
            });
            output.innerText = result;
        }

        selects.forEach(sel => {
            sel.addEventListener("change", () => {
                updateDropdowns();
                updateOutput();
            });
        });

        copyBtn.addEventListener("click", () => {
            navigator.clipboard.writeText(output.innerText);
            copyBtn.innerText = "Copied!";
            setTimeout(() => (copyBtn.innerText = "Copy"), 1000);
        });

        // Initial sync
        updateDropdowns();
        updateOutput();
    });
});

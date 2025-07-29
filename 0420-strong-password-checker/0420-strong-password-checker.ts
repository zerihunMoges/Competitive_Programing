

/**
 * Calculates the minimum number of operations (insert, delete, replace)
 * required to make a passphrase valid according to SecureCity's Sentinel policy.
 *
 * Sentinel’s Access Policy:
 * 1. Length Rule: Passphrase must be between 6 and 20 characters.
 * 2. Repetition Rule: No character may appear more than twice in a row.
 * 3. Complexity Rule: Must contain at least one uppercase letter, one lowercase letter, and one digit.
 *
 * @param passphrase - The input string to validate and fix.
 * @returns The minimum number of operations required to make the passphrase valid.
 */
export function strongPasswordChecker(passphrase: string): number {
  if (typeof passphrase !== 'string') return -1;

  const lowercase = new Set('abcdefghijklmnopqrstuvwxyz');
  const uppercase = new Set('ABCDEFGHIJKLMNOPQRSTUVWXYZ');
  const digit = new Set('0123456789');

  const characters = new Set(passphrase);

  const needsLowercase = ![...characters].some(c => lowercase.has(c));
  const needsUppercase = ![...characters].some(c => uppercase.has(c));
  const needsDigit = ![...characters].some(c => digit.has(c));
  const numRequiredTypeReplaces = Number(needsLowercase) + Number(needsUppercase) + Number(needsDigit);

  const len = passphrase.length;
  const numRequiredInserts = Math.max(0, 6 - len);
  const numRequiredDeletes = Math.max(0, len - 20);

  // Build list of repeated character group lengths
  const groups: number[] = [];
  for (let i = 0; i < len; ) {
    let j = i + 1;
    while (j < len && passphrase[j] === passphrase[i]) j++;
    groups.push(j - i);
    i = j;
  }

  // Apply best deletions to reduce repetition
  function applyBestDelete() {
    let minMod = Infinity;
    let idx = -1;

    for (let i = 0; i < groups.length; i++) {
      const group = groups[i];
      if (group >= 3) {
        const mod = group % 3;
        if (mod < minMod) {
          minMod = mod;
          idx = i;
        }
      }
    }

    if (idx !== -1) {
      groups[idx] -= 1;
    }
  }

  for (let i = 0; i < numRequiredDeletes; i++) {
    applyBestDelete();
  }

  const numRequiredGroupReplaces = groups.reduce((sum, group) => sum + Math.floor(group / 3), 0);

  return (
    numRequiredDeletes +
    Math.max(numRequiredTypeReplaces, numRequiredGroupReplaces, numRequiredInserts)
  );
}

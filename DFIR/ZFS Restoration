# ZFS Snapshot Restoration Process

### Steps to Restore and Backup ZFS Snapshots

#### Objective:
To restore ZFS snapshots incrementally, generate a unique list of file hashes, and back up the state of all files after each snapshot increment.

#### Process:

1. **Clean the ZFS Pool:**
    - Destroyed the existing `recoveredpool` to ensure a clean slate:
      ```bash
      sudo zfs destroy -r recoveredpool
      ```

2. **Restore Full Snapshot:**
    - Applied the first (full) snapshot to recreate the dataset:
      ```bash
      sudo zfs receive recoveredpool < logseq304481720128534
      ```

3. **Restore Incremental Snapshots and Recover Files:**
    - For each snapshot, restore the snapshot, hash the files, and back them up.
    - Code to achieve this:
      ```bash
      #!/bin/bash

      # List of snapshots (full + incremental) in the correct order
    snapshots=(
        "logseq304481720129999"  # Full snapshot (slightly changed)
        "logseq27444100618111-i"
        "logseq210022618026400-i"
        "logseq290521523729500-i"
        "logseq112462083415100-i"
        "logseq167161578611200-i"
        "logseq267652261217300-i"
        "logseq3161115304270-i"
        "logseq57352585531900-i"
        "logseq715093216905-i"
        "logseq23786207422060-i"
        "logseq175881536627000-i"
        "logseq132373269623100-i"
        "logseq316792317132200-i"
        "logseq2099802027940-i"
        "logseq28010819411800-i"
        "logseq123672701811800-i"
        "logseq26197855913000-i"
        "logseq165033087228200-i"
        "logseq23468810712900-i"
      )

      # Define the ZFS pool
      pool="recoveredpool"
      mountpoint="/recoveredpool"  # Replace this with the correct mount point of your dataset

      # Define the backup folder where files will be safely copied after each snapshot
      backup_dir="$HOME/safe_backup"

      # Create backup folder if it doesn't exist
      mkdir -p "$backup_dir"

      # File to store unique hashes
      hashes_file="$backup_dir/unique_hashes.txt"
      > "$hashes_file"  # Clear the file before starting

      # Iterate over the snapshots and apply them one by one
      for snapshot in "${snapshots[@]}"; do
        if [[ -f "$snapshot" ]]; then
          echo "Applying snapshot: $snapshot..."
          sudo zfs receive -F "$pool" < "$snapshot"

          # Calculate the hash of all files and store unique hashes
          echo "Calculating file hashes for snapshot $snapshot..."
          temp_hashes=$(mktemp)  # Temporary file to store current snapshot hashes
          find "$mountpoint" -type f -exec sha256sum {} \; > "$temp_hashes"

          # Add unique hashes to the main hash file
          cat "$temp_hashes" | awk '{print $1}' | sort | uniq >> "$hashes_file"

          # Make a backup of the files after applying this snapshot
          snapshot_backup_dir="$backup_dir/$(basename "$snapshot")"
          mkdir -p "$snapshot_backup_dir"
          echo "Backing up files to $snapshot_backup_dir..."
          cp -a "$mountpoint/." "$snapshot_backup_dir/"

          # Clean up temporary file
          rm "$temp_hashes"

          echo "Snapshot $snapshot applied and backed up."
        else
          echo "Snapshot file $snapshot not found, skipping..."
        fi
      done

      # Remove duplicate hashes from the main file
      sort -u "$hashes_file" -o "$hashes_file"
      ```

4. **Backup Files After Each Snapshot:**
    - Copied the current state of the files to a safe backup directory after each snapshot:
      ```bash
      cp -a /recoveredpool/. ~/safe_backup/[snapshot_name]/
      ```

5. **Final Clean-Up:**
    - Ensured all temporary files were removed and the list of hashes was deduplicated:
      ```bash
      sort -u unique_hashes.txt -o unique_hashes.txt
      ```

#### Results:
- Successfully restored the dataset incrementally.
- Safely backed up the state of all files at each snapshot increment in `~/safe_backup`.

#### Key Commands Used:
- `zfs destroy`
- `zfs receive`
- `find` (for recursive file listing)
- `cp -a` (for creating backups)
- `sort` and `uniq` (for deduplicating hashes)

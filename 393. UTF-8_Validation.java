class Solution {
    public boolean validUtf8(int[] data) {
        return validateUTF8(data);
    }
    
    int mask = (1 << 8) - 1;
    public int getLastByte(int var) {
        return (mask & var);
    }

    public boolean validateUTF8(int[] value) {
        int[] converted = new int[value.length];

        for(int i = 0; i < value.length; i++) {
            converted[i] = getLastByte(value[i]);
        }

        int k = 0;
        do {
            if (k >= converted.length) break;
            System.out.println("validating:" + converted[k] );
            if (getUtf8Length(converted[k]) == -1) {
                return  false;
            }
            switch (getUtf8Length(converted[k])) {
                case 1:
                    k++;
                    continue;
                case 2:
                    if (k+1 >= converted.length) {
                        return false;
                    }
                    if (!validateByte(converted[k+1])) {
                        return false;
                    }
                    k += 2;
                    System.out.println(k);
                    break;
                case 3:
                    for (int i = 0; i < 2;i++) {
                        if (k+1 + i >= converted.length) {
                            return false;
                        }
                        if (!validateByte(converted[k+1 + i])) {
                            return false;
                        }
                    }
                    k += 3;
                    break;
                case 4:
                    for (int i = 0; i < 3;i++) {
                        if (k+1 + i >= converted.length) {
                            return false;
                        }
                        if (!validateByte(converted[k+1 + i])) {
                            return false;
                        }
                    }
                    k += 4;
                    break;
            }

        } while (true);

        return true;
    }

    int byteMask = 0x80;//1000

    int getUtf8Length(int value) {

        int numberOfBytes = 0;
        if((value >> 7) == 0) { // 0xxxxxxx, 1 byte, 128(10000000)
            numberOfBytes = 1;
        } else if((value >> 5) == 0x06) {
            numberOfBytes = 2;
        } else if((value >> 4) == 0x0E) {
            numberOfBytes = 3;
        } else if((value >> 3) == 0x1E) { 
            numberOfBytes = 4;
        } else {
            return -1;
        }

        return numberOfBytes;
    }

    boolean validateByte(int value) {
        System.out.println("validateByte:" + Integer.toBinaryString(value) + ":" +
                ((value & byteMask) >> 6));
        if ((value & byteMask) >> 6 == 2) {
            return true;
        }
        return  false;
    }
}
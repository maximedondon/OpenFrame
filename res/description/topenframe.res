CONTAINER topenframe
{
    NAME topenframe;
    INCLUDE Tbase;

    GROUP OPENFRAME_MAIN_GROUP
    {
        DEFAULT 1;
        
        GROUP OPENFRAME_GROUP_RATIOS
        {
            DEFAULT 1;
            BOOL OPENFRAME_ENABLE_1_1 { }
            BOOL OPENFRAME_ENABLE_4_5 { }
            BOOL OPENFRAME_ENABLE_9_16 { }
            BOOL OPENFRAME_ENABLE_16_9 { }
            
            SEPARATOR { LINE; }
            BOOL OPENFRAME_ENABLE_CUSTOM { }
            GROUP
            {
                COLUMNS 2;
                REAL OPENFRAME_CUSTOM_W { MIN 1.0; STEP 1.0; }
                REAL OPENFRAME_CUSTOM_H { MIN 1.0; STEP 1.0; }
            }
        }
        
        GROUP OPENFRAME_GROUP_DISPLAY
        {
            DEFAULT 1;
            COLOR OPENFRAME_COLOR { }
        }
    }
}

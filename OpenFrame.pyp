import c4d
import os
from c4d import plugins, bitmaps

PLUGIN_ID = 1059999

# Resource IDs
OPENFRAME_ENABLE_1_1  = 2000
OPENFRAME_ENABLE_4_5  = 2001
OPENFRAME_ENABLE_9_16 = 2002
OPENFRAME_ENABLE_16_9 = 2003
OPENFRAME_ENABLE_CUSTOM = 2004
OPENFRAME_CUSTOM_W    = 2005
OPENFRAME_CUSTOM_H    = 2006
OPENFRAME_COLOR       = 2010

class OpenFrameTag(plugins.TagData):

    def Init(self, node, isCloneInit=False):
        if not isCloneInit:
            node[OPENFRAME_ENABLE_1_1]  = False
            node[OPENFRAME_ENABLE_4_5]  = False
            node[OPENFRAME_ENABLE_9_16] = False
            node[OPENFRAME_ENABLE_16_9] = False
            node[OPENFRAME_ENABLE_CUSTOM] = False
            node[OPENFRAME_CUSTOM_W]    = 1920.0
            node[OPENFRAME_CUSTOM_H]    = 800.0
            node[OPENFRAME_COLOR]       = c4d.Vector(0, 1, 0)
        return True

    def Draw(self, tag, op, bd, bh):
        # In C4D 2026, the tag is only being evaluated on pass 0 (DRAWPASS_OBJECT)
        if bd.GetDrawPass() != 0:
            return c4d.DRAWRESULT_SKIP

        # Only draw if the camera this tag is attached to is the active camera in this BaseDraw
        doc = tag.GetDocument()
        if bd.GetSceneCamera(doc) != op:
            return c4d.DRAWRESULT_SKIP

        # 1. Get Frame Data (C4D 2026 Dict support)
        frame = bd.GetFrame()
        if isinstance(frame, dict):
            fl, ft, fr, fb = frame['cl'], frame['ct'], frame['cr'], frame['cb']
        else:
            fl, ft, fr, fb = frame
            
        safe_frame = bd.GetSafeFrame()
        if isinstance(safe_frame, dict):
            sl, st, sr, sb = safe_frame['cl'], safe_frame['ct'], safe_frame['cr'], safe_frame['cb']
        else:
            sl, st, sr, sb = safe_frame
            
        sw, sh = sr - sl, sb - st
        if sw <= 0 or sh <= 0:
            sl, st, sr, sb = fl, ft, fr, fb
            sw, sh = sr - sl, sb - st
            
        if sw <= 0 or sh <= 0: return c4d.DRAWRESULT_SKIP

        cx, cy = (sl + sr) / 2.0, (st + sb) / 2.0
        
        # 2. Prepare Viewport for 2D Screen Space
        bd.SetMatrix_Screen()
        
        color = tag[OPENFRAME_COLOR]
        if not isinstance(color, c4d.Vector): color = c4d.Vector(0, 1, 0)
        bd.SetPen(color)

        # 3. Calculate Ratios
        targets = []
        if tag[OPENFRAME_ENABLE_1_1]:  targets.append(1.0)
        if tag[OPENFRAME_ENABLE_4_5]:  targets.append(4.0/5.0)
        if tag[OPENFRAME_ENABLE_9_16]: targets.append(9.0/16.0)
        if tag[OPENFRAME_ENABLE_16_9]: targets.append(16.0/9.0)
        
        if tag[OPENFRAME_ENABLE_CUSTOM]:
            cw = tag[OPENFRAME_CUSTOM_W]
            ch = tag[OPENFRAME_CUSTOM_H]
            if cw > 0 and ch > 0:
                targets.append(float(cw) / float(ch))

        render_ratio = float(sw) / float(sh)
        
        # 4. Draw Lines
        for target_ratio in targets:
            if target_ratio > render_ratio:
                w, h = sw, sw / target_ratio
            else:
                h, w = sh, sh * target_ratio
                
            x1, y1 = cx - w/2.0, cy - h/2.0
            x2, y2 = cx + w/2.0, cy + h/2.0
            
            bd.DrawLine2D(c4d.Vector(x1, y1, 0), c4d.Vector(x2, y1, 0))
            bd.DrawLine2D(c4d.Vector(x2, y1, 0), c4d.Vector(x2, y2, 0))
            bd.DrawLine2D(c4d.Vector(x2, y2, 0), c4d.Vector(x1, y2, 0))
            bd.DrawLine2D(c4d.Vector(x1, y2, 0), c4d.Vector(x1, y1, 0))
            
        return c4d.DRAWRESULT_OK


if __name__ == "__main__":
    # Determine the correct registration flags
    flags = c4d.TAG_EXPRESSION | c4d.TAG_VISIBLE
    
    # In some C4D versions, this explicit flag is required for Draw() to be called.
    if hasattr(c4d, 'TAG_IMPLEMENTS_DRAW_FUNCTION'):
        flags |= getattr(c4d, 'TAG_IMPLEMENTS_DRAW_FUNCTION')

    # Load the icon
    icon_path = os.path.join(os.path.dirname(__file__), "res", "icon.png")
    bmp = bitmaps.BaseBitmap()
    if os.path.exists(icon_path):
        bmp.InitWith(icon_path)
    else:
        bmp = None

    plugins.RegisterTagPlugin(id=PLUGIN_ID,
                              str="Open Frame",
                              info=flags,
                              g=OpenFrameTag,
                              description="topenframe",
                              icon=bmp)
